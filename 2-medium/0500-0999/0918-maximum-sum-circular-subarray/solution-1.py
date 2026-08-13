from typing import List

# two kadane

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globMax = globMin = nums[0]
        currMax = currMin = 0
        total = 0

        for x in nums:
            currMax = max(currMax + x, x)
            currMin = min(currMin + x, x)
            globMax = max(globMax, currMax)
            globMin = min(globMin, currMin)
            total += x

        return max(globMax, total - globMin) if globMax > 0 else globMax