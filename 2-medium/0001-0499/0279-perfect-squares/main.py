class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n] * (n + 1)
        dp[0] = 0

        for t in range(1, n + 1):
            for s in range(1, t + 1):
                square = s ** 2
                if t < square: break
                dp[t] = min(dp[t], 1 + dp[t - square])
        
        return dp[n]