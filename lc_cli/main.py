from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import requests
from dotenv import load_dotenv


ROOT_DIR = Path(__file__).resolve().parents[1]
DEFAULT_API_BASE_URL = "https://leetcode-mcp-3in743b2uq-uc.a.run.app"

DIFFICULTY_DIRS = {
    "Easy": "1-easy",
    "Medium": "2-medium",
    "Hard": "3-hard",
}

LANG_EXTENSIONS = {
    "bash": "sh",
    "c": "c",
    "csharp": "cs",
    "cpp": "cpp",
    "dart": "dart",
    "elixir": "ex",
    "erlang": "erl",
    "golang": "go",
    "java": "java",
    "javascript": "js",
    "kotlin": "kt",
    "mssql": "sql",
    "mysql": "sql",
    "oraclesql": "sql",
    "pandas": "py",
    "php": "php",
    "postgresql": "sql",
    "python": "py",
    "python3": "py",
    "racket": "rkt",
    "ruby": "rb",
    "rust": "rs",
    "scala": "scala",
    "swift": "swift",
    "typescript": "ts",
}

SOLUTION_FILE_RE = re.compile(r"^solution-[1-9]\d*\.[^.]+$")


class LcError(Exception):
    pass


@dataclass(frozen=True)
class ApiClient:
    base_url: str
    api_key: str

    @classmethod
    def from_env(cls) -> "ApiClient":
        load_dotenv(ROOT_DIR / ".env")
        base_url = os.getenv("LEETCODE_API_BASE_URL", DEFAULT_API_BASE_URL).rstrip("/")
        api_key = os.getenv("LEETCODE_API_KEY")
        if not api_key:
            raise LcError("LEETCODE_API_KEY is missing. Add it to .env or your shell environment.")
        return cls(base_url=base_url, api_key=api_key)

    def get(self, path: str) -> dict[str, Any]:
        url = f"{self.base_url}{path}"
        try:
            response = requests.get(
                url,
                headers={"Authorization": f"Bearer {self.api_key}"},
                timeout=20,
            )
        except requests.RequestException as exc:
            raise LcError(f"request failed for {path}: {exc}") from exc

        if response.ok:
            return response.json()

        try:
            payload = response.json()
            message = payload.get("error", {}).get("message") or response.text
            code = payload.get("error", {}).get("code")
        except ValueError:
            message = response.text
            code = None

        if code:
            raise LcError(f"{code}: {message}")
        raise LcError(f"HTTP {response.status_code}: {message}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="lc", description="LeetCode repo DX helpers")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="create a problem folder, README, and starter solution")
    add_parser.add_argument("problem_id", type=parse_problem_id, help="numeric LeetCode frontend ID")
    add_parser.add_argument("lang_slug", help="LeetCode language slug, for example python3 or postgresql")
    add_parser.add_argument("--force-readme", action="store_true", help="regenerate README.md if it exists")
    add_parser.add_argument("--no-open", action="store_true", help="do not open files in VS Code after writing")
    add_parser.set_defaults(func=add_problem)

    done_parser = subparsers.add_parser("done", help="stage and commit one completed problem")
    done_parser.add_argument("problem_id", type=parse_problem_id, help="numeric LeetCode frontend ID")
    done_parser.add_argument("--message", "-m", help='commit message, default: "add q<id>"')
    done_parser.add_argument("--push", action="store_true", help="push after a successful commit")
    done_parser.add_argument("--dry-run", action="store_true", help="show what would be committed without staging")
    done_parser.set_defaults(func=done_problem)

    return parser


def parse_problem_id(value: str) -> int:
    try:
        problem_id = int(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("problem ID must be an integer") from exc
    if problem_id <= 0:
        raise argparse.ArgumentTypeError("problem ID must be positive")
    return problem_id


def add_problem(args: argparse.Namespace) -> int:
    client = ApiClient.from_env()
    problem = fetch_problem(client, args.problem_id)
    snippets = fetch_snippets(client, args.problem_id)
    snippet = select_snippet(snippets, args.lang_slug)

    extension = LANG_EXTENSIONS.get(args.lang_slug)
    if not extension:
        available_known = ", ".join(sorted(LANG_EXTENSIONS))
        raise LcError(
            f'langSlug "{args.lang_slug}" needs a file extension mapping. '
            f"Known mappings: {available_known}"
        )

    problem_dir = canonical_problem_dir(problem)
    existing = find_existing_problem_dirs(args.problem_id)
    unexpected = [path for path in existing if path != problem_dir]
    if unexpected:
        paths = "\n".join(f"  - {path.relative_to(ROOT_DIR)}" for path in unexpected)
        raise LcError(
            "found existing folder(s) for this problem outside the canonical path:\n"
            f"{paths}\n"
            f"expected: {problem_dir.relative_to(ROOT_DIR)}\n"
            "not moving anything automatically."
        )

    if problem_dir.exists() and not problem_dir.is_dir():
        raise LcError(f"canonical path exists but is not a directory: {problem_dir}")

    problem_dir.mkdir(parents=True, exist_ok=True)

    readme_path = problem_dir / "README.md"
    wrote_readme = write_readme(readme_path, problem, force=args.force_readme)

    solution_path = next_solution_path(problem_dir, extension)
    solution_path.write_text(snippet["code"].rstrip() + "\n", encoding="utf-8")

    print(f"problem: {problem['id']}. {problem['title']}")
    print(f"folder:  {problem_dir.relative_to(ROOT_DIR)}")
    print(f"readme:  {'wrote' if wrote_readme else 'kept'} README.md")
    print(f"code:    wrote {solution_path.name}")

    if not args.no_open:
        open_in_vscode(solution_path, readme_path)

    return 0


def done_problem(args: argparse.Namespace) -> int:
    problem_dir = resolve_local_problem_dir(args.problem_id)
    validate_done_problem_dir(problem_dir)

    message = args.message or f"add q{args.problem_id}"
    changed_paths = git_changed_paths(problem_dir)

    print(f"problem: q{args.problem_id}")
    print(f"folder:  {problem_dir.relative_to(ROOT_DIR)}")

    if not changed_paths:
        print("nothing to commit for this problem")
        return 0

    print("changes:")
    for path in changed_paths:
        print(f"  {path}")
    print(f"commit:  {message}")

    outside_staged = git_staged_paths_outside(problem_dir)
    if outside_staged:
        print("note: unrelated staged changes exist and will be left untouched:")
        for path in outside_staged:
            print(f"  {path}")

    if args.dry_run:
        print("dry run: skipped git add/commit")
        return 0

    git_run(["add", "-A", "--", str(problem_dir.relative_to(ROOT_DIR))])

    if git_run(["diff", "--cached", "--quiet", "--", str(problem_dir.relative_to(ROOT_DIR))], check=False).returncode == 0:
        print("nothing to commit for this problem")
        return 0

    git_run(["commit", "-m", message, "--", str(problem_dir.relative_to(ROOT_DIR))])
    print("committed")

    if args.push:
        git_run(["push"])
        print("pushed")

    return 0


def resolve_local_problem_dir(problem_id: int) -> Path:
    matches = find_existing_problem_dirs(problem_id)
    if not matches:
        raise LcError(f"q{problem_id} is not present locally. Run `uv run lc add {problem_id} <langSlug>` first.")
    if len(matches) > 1:
        paths = "\n".join(f"  - {path.relative_to(ROOT_DIR)}" for path in matches)
        raise LcError(f"multiple folders match q{problem_id}:\n{paths}")
    return matches[0]


def validate_done_problem_dir(problem_dir: Path) -> None:
    readme_path = problem_dir / "README.md"
    if not readme_path.is_file():
        raise LcError(f"{problem_dir.relative_to(ROOT_DIR)} is missing README.md")

    solution_paths = sorted(path for path in problem_dir.iterdir() if path.is_file() and SOLUTION_FILE_RE.match(path.name))
    if not solution_paths:
        raise LcError(
            f"{problem_dir.relative_to(ROOT_DIR)} has no solution files. "
            "Expected at least one file matching solution-*.*"
        )

    nonconvention_files = []
    for path in sorted(item for item in problem_dir.iterdir() if item.is_file()):
        if path.name == "README.md" or SOLUTION_FILE_RE.match(path.name):
            continue
        if is_git_ignored(path):
            continue
        nonconvention_files.append(path.name)

    if nonconvention_files:
        names = "\n".join(f"  - {name}" for name in nonconvention_files)
        raise LcError(f"folder has non-convention files that Git would track:\n{names}")


def git_changed_paths(problem_dir: Path) -> list[str]:
    result = git_run(["status", "--short", "--", str(problem_dir.relative_to(ROOT_DIR))], capture=True)
    return [line for line in result.stdout.splitlines() if line.strip()]


def git_staged_paths_outside(problem_dir: Path) -> list[str]:
    result = git_run(["diff", "--cached", "--name-only"], capture=True)
    prefix = f"{problem_dir.relative_to(ROOT_DIR)}/"
    return [path for path in result.stdout.splitlines() if path and path != str(problem_dir.relative_to(ROOT_DIR)) and not path.startswith(prefix)]


def is_git_ignored(path: Path) -> bool:
    return git_run(["check-ignore", "-q", "--", str(path.relative_to(ROOT_DIR))], check=False).returncode == 0


def git_run(
    args: list[str],
    *,
    capture: bool = False,
    check: bool = True,
) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(
        ["git", *args],
        cwd=ROOT_DIR,
        text=True,
        capture_output=capture,
        check=False,
    )
    if check and result.returncode != 0:
        detail = (result.stderr or result.stdout).strip()
        command = "git " + " ".join(args)
        if detail:
            raise LcError(f"{command} failed: {detail}")
        raise LcError(f"{command} failed with exit code {result.returncode}")
    return result


def fetch_problem(client: ApiClient, problem_id: int) -> dict[str, Any]:
    payload = client.get(f"/api/problems/id/{problem_id}")
    problem = payload.get("problem")
    if not problem:
        raise LcError(f"problem {problem_id} was not found")
    return problem


def fetch_snippets(client: ApiClient, problem_id: int) -> list[dict[str, Any]]:
    payload = client.get(f"/api/problems/id/{problem_id}/code-snippets")
    snippets = payload.get("code_snippets")
    if not isinstance(snippets, list):
        raise LcError(f"code snippet response for problem {problem_id} was malformed")
    return snippets


def select_snippet(snippets: list[dict[str, Any]], lang_slug: str) -> dict[str, Any]:
    for snippet in snippets:
        if snippet.get("langSlug") == lang_slug:
            code = snippet.get("code")
            if not isinstance(code, str) or not code.strip():
                raise LcError(f'langSlug "{lang_slug}" has an empty starter snippet')
            return snippet

    available = sorted(slug for slug in (s.get("langSlug") for s in snippets) if isinstance(slug, str))
    if available:
        raise LcError(
            f'problem does not support langSlug "{lang_slug}". '
            f"Available: {', '.join(available)}"
        )
    raise LcError("problem has no available code snippets")


def canonical_problem_dir(problem: dict[str, Any]) -> Path:
    problem_id = int(problem["id"])
    difficulty = problem.get("difficulty")
    difficulty_dir = DIFFICULTY_DIRS.get(difficulty)
    if not difficulty_dir:
        raise LcError(f'unknown difficulty "{difficulty}" for problem {problem_id}')

    slug = problem.get("slug")
    if not isinstance(slug, str) or not slug:
        raise LcError(f"problem {problem_id} is missing a slug")

    return ROOT_DIR / difficulty_dir / range_dir_for(problem_id) / f"{problem_id:04d}-{slug}"


def range_dir_for(problem_id: int) -> str:
    if problem_id < 500:
        return "0001-0499"
    start = (problem_id // 500) * 500
    end = start + 499
    return f"{start:04d}-{end:04d}"


def find_existing_problem_dirs(problem_id: int) -> list[Path]:
    prefix = f"{problem_id:04d}-"
    matches: list[Path] = []
    for difficulty_dir in DIFFICULTY_DIRS.values():
        root = ROOT_DIR / difficulty_dir
        if not root.exists():
            continue
        for range_path in root.iterdir():
            if not range_path.is_dir():
                continue
            matches.extend(path for path in range_path.glob(f"{prefix}*") if path.is_dir())
    return sorted(set(matches))


def write_readme(readme_path: Path, problem: dict[str, Any], force: bool) -> bool:
    if readme_path.exists() and not force:
        return False
    readme_path.write_text(format_readme(problem), encoding="utf-8")
    return True


def format_readme(problem: dict[str, Any]) -> str:
    lines = [
        f"# {problem['id']}. {problem['title']}",
        "",
        f"**Difficulty:** {problem['difficulty']}",
        "",
    ]

    tags = problem.get("tags") or []
    if tags:
        lines.extend([f"**Tags:** {', '.join(f'`{tag}`' for tag in tags)}", ""])

    if problem.get("is_premium"):
        lines.extend(["**Premium:** Yes", ""])

    lines.extend(["---", "", "## Description", ""])
    content_md = problem.get("content_md")
    if isinstance(content_md, str) and content_md.strip():
        lines.extend([content_md.strip(), ""])
    else:
        lines.extend(["_No description available from the LeetCode API._", ""])

    hints = problem.get("hints") or []
    if hints:
        lines.extend(["---", "", "## Hints", ""])
        for index, hint in enumerate(hints, start=1):
            lines.extend(
                [
                    "<details>",
                    f"<summary>Hint {index}</summary>",
                    "",
                    str(hint).strip(),
                    "</details>",
                    "",
                ]
            )

    return "\n".join(lines).rstrip() + "\n"


def next_solution_path(problem_dir: Path, extension: str) -> Path:
    index = 1
    while True:
        candidate = problem_dir / f"solution-{index}.{extension}"
        if not candidate.exists():
            return candidate
        index += 1


def open_in_vscode(solution_path: Path, readme_path: Path) -> None:
    try:
        subprocess.run(
            ["code", "--reuse-window", str(solution_path), str(readme_path)],
            cwd=ROOT_DIR,
            check=False,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    except FileNotFoundError:
        print("note: VS Code CLI `code` was not found; skipped opening files.")


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    try:
        raise SystemExit(args.func(args))
    except LcError as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc


if __name__ == "__main__":
    main()
