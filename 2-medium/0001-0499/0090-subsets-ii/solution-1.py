from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        path = []
        n = len(nums)

        def backtrack(start):
            ans.append(path.copy())
            
            for i in range(start, n):
                if i > start and nums[i] == nums[i - 1]: continue
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()

        backtrack(0)
        return ans