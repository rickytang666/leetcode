from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = curr = nums[0]
        for i in range(1, len(nums)):
            curr = max(curr + nums[i], nums[i])
            ans = max(curr, ans)
        return ans