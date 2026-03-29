from typing import List

# 2d dp but rolling array

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        s = sum(nums)

        if target > s or target < -s:
            return 0
        
        prev = [0] * (2 * s + 1)
        prev[s] = 1

        for x in nums:
            curr = [0] * (2 * s + 1)
            for j in range(2 * s + 1):
                if j - x >= 0:
                    curr[j] += prev[j - x]
                if j + x < 2 * s + 1:
                    curr[j] += prev[j + x]
            prev = curr
        
        return prev[s + target]