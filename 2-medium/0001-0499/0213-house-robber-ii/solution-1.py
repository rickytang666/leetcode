from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_normal(arr):
            prev2 = prev1 = 0
            for a in arr:
                curr = max(prev1, prev2 + a)
                prev2 = prev1
                prev1 = curr
            return prev1
        n = len(nums)
        if n == 1: return nums[0]
        return max(rob_normal(nums[:-1]), rob_normal(nums[1:]))