from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        def backtrack(path, used):
            if len(path) == n:
                ans.append(path.copy())
                return
            for i in range(n):
                if used[i]: continue
                path.append(nums[i])
                used[i] = True
                backtrack(path, used)
                path.pop()
                used[i] = False
        backtrack([], [False] * n)
        return ans