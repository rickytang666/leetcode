from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = sum = i = 0
        for j in range(len(nums)):
            sum += nums[j]
            if sum < j - i:
                sum -= nums[i]
                i += 1
            ans = max(ans, j - i)
        return ans