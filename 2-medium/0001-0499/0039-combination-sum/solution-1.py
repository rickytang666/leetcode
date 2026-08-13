from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        n = len(candidates)
        candidates.sort()

        def backtrack(start, remaining, path):
            if remaining == 0:
                self.ans.append(path.copy())
                return
            if remaining < 0:
                return
            for i in range(start, n):
                path.append(candidates[i])
                backtrack(i, remaining - candidates[i], path)
                path.pop()
        
        backtrack(0, target, [])
        return self.ans