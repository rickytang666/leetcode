from typing import List

# top-down dp
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        memo = {}
        def rec(i, holding):
            if i == n: return 0
            if (i, holding) in memo: return memo[(i, holding)]
            ans = rec(i + 1, holding)
            if holding:
                ans = max(ans, prices[i] + rec(i + 1, False))
            else:
                ans = max(ans, -prices[i] + rec(i + 1, True))
            memo[(i, holding)] = ans
            return ans
        return rec(0, False)