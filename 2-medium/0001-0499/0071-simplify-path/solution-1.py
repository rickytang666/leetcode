class Solution:
    def simplifyPath(self, path: str) -> str:
        ans = []
        parts = path.split('/')
        for p in parts:
            if p == '..':
                if ans:
                    ans.pop()
            elif p != '' and p != '.':
                ans.append(p)
        return '/' + '/'.join(ans)