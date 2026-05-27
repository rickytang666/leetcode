import os
import requests
import json
import argparse
import sys
import subprocess
import re
from markdownify import markdownify as md

# ANSI color codes
RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"

# constants
LEETCODE_GRAPHQL_URL = "https://leetcode.com/graphql"
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # parent of fetch-readmes
CACHE_FILE = os.path.join(ROOT_DIR, "fetch-readmes", "id_map.json")

HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
}

# query to fetch all questions for id -> slug mapping
ALL_QUESTIONS_QUERY = """
query problemsetQuestionList($limit: Int, $skip: Int) {
    problemsetQuestionList: questionList(
        categorySlug: ""
        limit: $limit
        skip: $skip
        filters: {}
    ) {
        questions: data {
            questionFrontendId
            titleSlug
        }
    }
}
"""


# query to fetch specific question details
QUESTION_DATA_QUERY = """
query questionData($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionId
    questionFrontendId
    title
    titleSlug
    content
    difficulty
    likes
    dislikes
    topicTags {
      name
      slug
    }
    stats
    hints
  }
}
"""

def build_id_to_slug_map(force_refresh=False):
    # try loading from cache first
    if not force_refresh and os.path.exists(CACHE_FILE):
        try:
            print("loading id map from cache...")
            with open(CACHE_FILE, "r") as f:
                id_map = json.load(f)
            print(f"loaded {len(id_map)} problems from cache.")
            return id_map
        except Exception:
            print("cache invalid, fetching from remote...")

    print("fetching global problem list for id mapping...")
    
    id_map = {}
    limit = 100
    skip = 0
    
    while True:
        payload = {
            "operationName": "problemsetQuestionList",
            "variables": {"limit": limit, "skip": skip},
            "query": ALL_QUESTIONS_QUERY
        }
        
        try:
            response = requests.post(LEETCODE_GRAPHQL_URL, json=payload, headers=HEADERS, timeout=30)
            response.raise_for_status()
            data = response.json()
            questions = data.get("data", {}).get("problemsetQuestionList", {}).get("questions", [])
            
            if not questions:
                break
                
            for q in questions:
                fid = q.get("questionFrontendId")
                slug = q.get("titleSlug")
                if fid and slug:
                    id_map[str(fid)] = slug
            
            print(f"fetched {len(questions)} problems (total: {len(id_map)})")
            
            if len(questions) < limit:
                break
                
            skip += limit
            
        except requests.exceptions.RequestException as e:
            print(f"error fetching problem list: {e}")
            break
            
    print(f"loaded {len(id_map)} problems into map.")
    
    # save to cache
    try:
        with open(CACHE_FILE, "w") as f:
            json.dump(id_map, f)
        print("saved id map to cache.")
    except Exception as e:
        print(f"{RED}warning: failed to save cache: {e}{RESET}")
        
    return id_map

def get_question_details(title_slug):
    payload = {
        "operationName": "questionData",
        "variables": {"titleSlug": title_slug},
        "query": QUESTION_DATA_QUERY
    }
    
    try:
        response = requests.post(LEETCODE_GRAPHQL_URL, json=payload, headers=HEADERS, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data.get("data", {}).get("question")
    except requests.exceptions.RequestException as e:
        print(f"error fetching data for {title_slug}: {e}")
        return None

def format_readme(question_data):
    if not question_data:
        return None

    title = question_data.get("title")
    difficulty = question_data.get("difficulty")
    frontend_id = question_data.get("questionFrontendId")
    content_html = question_data.get("content") or ""
    topic_tags = question_data.get("topicTags", [])
    hints = question_data.get("hints", [])
    try:
        stats = json.loads(question_data.get("stats", "{}"))
        acceptance_rate = stats.get("acRate", "N/A")
    except Exception:
        acceptance_rate = "N/A"

    markdown_content = f"# {frontend_id}. {title}\n\n"
    markdown_content += f"**Difficulty:** {difficulty}\n\n"
    markdown_content += f"**Acceptance Rate:** {acceptance_rate}\n\n"
    
    if topic_tags:
        tags_str = ", ".join([f"`{tag['name']}`" for tag in topic_tags])
        markdown_content += f"**Tags:** {tags_str}\n\n"
        
    markdown_content += "---\n\n"
    markdown_content += "## Description\n\n"
    markdown_content += md(content_html)
    
    if hints:
        markdown_content += "\n\n---\n\n"
        markdown_content += "## Hints\n\n"
        for i, hint in enumerate(hints, 1):
            markdown_content += f"<details>\n<summary>Hint {i}</summary>\n\n{hint}\n</details>\n\n"

    return markdown_content

def process_problem(problem_path, folder_name, id_map):
    try:
        # check if readme exists
        if os.path.exists(os.path.join(problem_path, "README.md")):
            return False, False
            
        # extract id from folder name (e.g. 0001-two-sum -> 1)
        parts = folder_name.split("-", 1)
        if len(parts) < 2 or not parts[0].isdigit():
            return False, False
        
        folder_id_str = parts[0]
        # remove leading zeros for map lookup (0001 -> 1)
        # but keep as string because map keys are strings
        lookup_id = str(int(folder_id_str))
        
        title_slug = id_map.get(lookup_id)
        
        # fallback: if not in map, try to use the slug from folder name?
        # current decision: prioritize map. if not in map, might be stale id or new problem script hasn't seen?
        # let's try fallback to folder name slug if map lookup fails, but warn.
        warning_occurred = False
        if not title_slug:
            title_slug = parts[1]
            print(f"{RED}warning: id {lookup_id} not found in map. trying slug from folder: {title_slug}{RESET}")
            warning_occurred = True
        else:
            print(f"processing: {folder_name} -> id: {lookup_id} -> slug: {title_slug}")
        
        question_data = get_question_details(title_slug)
        if not question_data:
            print(f"{RED}failed to get info for {title_slug}{RESET}")
            return False, True
            
        readme_content = format_readme(question_data)
        if readme_content:
            target_path = os.path.join(problem_path, "README.md")
            with open(target_path, "w", encoding="utf-8") as f:
                f.write(readme_content)
            print(f"generated readme for {folder_name}")
            return True, warning_occurred
                
        return False, True
    except Exception as e:
        print(f"{RED}Error processing {folder_name}: {e}{RESET}")
        return False, True

def get_changed_dirs():
    """returns a set of absolute paths for directories that have changed (git status)"""
    print("checking git status for changed files...")
    try:
        # get status of all files (porcelain is stable output-friendly)
        result = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True, cwd=ROOT_DIR)
        
        changed_problem_dirs = set()
        
        # regex to identify non-problem folders
        # 1-easy, 2-medium, 3-hard
        category_re = re.compile(r"^\d+-(easy|medium|hard)$")
        # 0001-0499 (range folders)
        range_re = re.compile(r"^\d+-\d+$")
        
        # parse output lines like " M some/file.py" or "?? new/file.py"
        for line in result.stdout.splitlines():
            if len(line.strip()) < 3:
                continue
            
            # path is usually from char 3 to end
            rel_path = line[3:].strip()
            # handle rename cases like "R  old -> new"
            if " -> " in rel_path: 
                rel_path = rel_path.split(" -> ")[-1]
                
            abs_path = os.path.abspath(os.path.join(ROOT_DIR, rel_path))
            
            # traverse up the path to find the 'problem folder'
            # we look for any directory component that starts with a digit
            # and is NOT a category or range folder
            
            # split path into components relative to root to avoid scanning /Users/...
            try:
                rel_parts = os.path.relpath(abs_path, ROOT_DIR).split(os.sep)
            except ValueError:
                continue # path not relative to root?
            
            current_scan_path = ROOT_DIR
            for part in rel_parts:
                current_scan_path = os.path.join(current_scan_path, part)
                
                # check if this part looks like a potential problem folder
                if part[0].isdigit():
                    if category_re.match(part):
                        continue
                    if range_re.match(part):
                        continue
                    
                    # if we are here, it starts with digit and isn't a structural folder
                    # it's likely a problem folder (e.g. 0001-two-sum, 0098-validate...)
                    if os.path.isdir(current_scan_path):
                        changed_problem_dirs.add(current_scan_path)
                        
        print(f"found {len(changed_problem_dirs)} changed problem directories.")
        return changed_problem_dirs
        
    except Exception as e:
        print(f"{RED}error checking git status: {e}{RESET}")
        return set()

def main():
    parser = argparse.ArgumentParser(description="fetch leetcode readmes")
    parser.add_argument("--test", action="store_true", help="run on a single problem and exit")
    parser.add_argument("--new", action="store_true", help="run only on newly added/modified problems (git status)")
    parser.add_argument("--refresh", action="store_true", help="force refresh of the id mapping cache")
    args = parser.parse_args()

    # build global map first
    id_map = build_id_to_slug_map(force_refresh=args.refresh)
    if not id_map:
        print("failed to build id map. exiting.")
        sys.exit(1)
        
    target_dirs = None
    if args.new:
        target_dirs = get_changed_dirs()
        if not target_dirs:
            print("no changes detected via git status. exiting.")
            sys.exit(0)
        
        # directly iterate over the identified target directories
        print(f"processing {len(target_dirs)} detected problem folders...")
        any_failure = False
        for problem_path in target_dirs:
            if not os.path.isdir(problem_path):
                continue
            folder_name = os.path.basename(problem_path)
            success, error = process_problem(problem_path, folder_name, id_map)
            if error:
                any_failure = True
            if args.test and success:
                print("test mode enabled. stopping after first success.")
                sys.exit(0)
        
        if not any_failure:
            print(f"{GREEN}all done!{RESET}")
        return

    # folders to scan (depth 1)
    difficulty_dirs = ["1-easy", "2-medium", "3-hard"]
    
    print("starting scan...")
    
    any_failure = False

    for diff_dir in difficulty_dirs:
        diff_path = os.path.join(ROOT_DIR, diff_dir)
        if not os.path.exists(diff_path):
            continue
            
        # depth 2: range folders (sorted)
        range_dirs = sorted(os.listdir(diff_path))
        for range_dir in range_dirs:
            range_path = os.path.join(diff_path, range_dir)
            if not os.path.isdir(range_path) or range_dir.startswith("."):
                continue
                
            # depth 3: problem folders (sorted)
            problem_dirs = sorted(os.listdir(range_path))
            for problem_dir in problem_dirs:
                problem_path = os.path.join(range_path, problem_dir)
                if not os.path.isdir(problem_path) or problem_dir.startswith("."):
                    continue
                
                success, error = process_problem(problem_path, problem_dir, id_map)
                if error:
                    any_failure = True

                if args.test and success:
                    print("test mode enabled. stopping after first success.")
                    sys.exit(0)
    
    if not any_failure:
        print(f"{GREEN}all done!{RESET}")

if __name__ == "__main__":
    main()
