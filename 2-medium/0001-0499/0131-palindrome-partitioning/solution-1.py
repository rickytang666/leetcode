from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        path = []
        n = len(s)
        def check(a):
            return a == a[::-1]
        def backtracK(start):
            if start == n:
                ans.append(path.copy())
                return
            for end in range(start, n):
                substr = s[start:end + 1]
                if check(substr):
                    path.append(substr)
                    backtracK(end + 1)
                    path.pop()
        backtracK(0)
        return ans