from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def isFeasible(cap):
            cnt = 1
            curr = cap
            for w in weights:
                if curr < w:
                    cnt += 1
                    curr = cap
                curr -= w

            return cnt <= days
        
        lo, hi = max(weights), sum(weights)
        ans = hi
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if isFeasible(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return ans