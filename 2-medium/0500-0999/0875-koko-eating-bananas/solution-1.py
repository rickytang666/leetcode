from typing import List
from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(k):
            return sum(ceil(pile / k) for pile in piles) <= h
        left, right = 1, max(piles)
        if h == len(piles): return right
        ans = right

        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans