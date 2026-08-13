from typing import List

# 2d dp

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        s = sum(nums)
        n = len(nums)

        if target > s or target < -s:
            return 0
        
        dp = [[0] * (s * 2 + 1) for _ in range(n + 1)]
        dp[0][s] = 1

        for i in range(1, n + 1):
            for j in range(s * 2 + 1):
                if j - nums[i-1] >= 0:
                    dp[i][j] += dp[i-1][j - nums[i-1]]
                if j + nums[i-1] < s * 2 + 1:
                    dp[i][j] += dp[i-1][j + nums[i-1]]
        
        return dp[n][target + s]