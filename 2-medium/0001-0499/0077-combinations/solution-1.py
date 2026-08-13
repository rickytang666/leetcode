from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def backtrack(start, path):
            if len(path) == k:
                ans.append(path.copy())
                return
            
            for i in range(start + 1, n + 1):
                path.append(i)
                backtrack(i, path)
                path.pop()
        
        backtrack(0, [])

        return ans