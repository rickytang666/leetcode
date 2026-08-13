from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold, sold, free = -prices[0], float('-inf'), 0

        for p in prices[1:]:
            prev_hold, prev_sold, prev_free = hold, sold, free
            hold = max(prev_hold, prev_free - p)
            sold = prev_hold + p
            free = max(prev_free, prev_sold)
        
        return max(sold, free)
