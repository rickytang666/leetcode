from typing import List

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue) 
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        def rangeSum(i, j):
            return prefix[j + 1] - prefix[i]

        dp = [[0] * n for _ in range(n)]
        preMax = [[0] * n for _ in range(n)]
        sufMax = [[0] * n for _ in range(n)]

        for i in range(n):
            preMax[i][i] = stoneValue[i]
            sufMax[i][i] = stoneValue[i]

        for length in range(1, n):
            for i in range(0, n - length):
                j = i + length

                lo, hi, k_mid = i, j - 1, i - 1
                while lo <= hi:
                    mid = lo + (hi - lo) // 2
                    if rangeSum(i, mid) <= rangeSum(mid + 1, j):
                        k_mid = mid
                        lo = mid + 1
                    else:
                        hi = mid - 1

                best = 0
                if k_mid >= i:
                    best = max(best, preMax[i][k_mid])
                right_start = k_mid + 2
                if k_mid >= i and rangeSum(i, k_mid) == rangeSum(k_mid + 1, j):
                    right_start = k_mid + 1

                if right_start <= j:
                    best = max(best, sufMax[j][right_start])

                dp[i][j] = best
                preMax[i][j] = max(preMax[i][j - 1], dp[i][j] + rangeSum(i, j))
                sufMax[j][i] = max(sufMax[j][i + 1], dp[i][j] + rangeSum(i, j))

        return dp[0][n - 1] if n > 1 else 0