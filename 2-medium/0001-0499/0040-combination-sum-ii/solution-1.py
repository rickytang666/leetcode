from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        n = len(candidates)

        def backtrack(start, remaining, path):
            if remaining == 0:
                ans.append(path.copy())
                return
            if remaining < 0:
                return
            for i in range(start, n):
                if i > start and candidates[i] == candidates[i - 1]: continue
                
                path.append(candidates[i])
                backtrack(i + 1, remaining - candidates[i], path)
                path.pop()

        backtrack(0, target, [])
        return ans