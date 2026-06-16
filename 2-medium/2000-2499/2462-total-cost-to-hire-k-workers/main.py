from typing import List
import heapq

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        left, right = candidates - 1, max(candidates, len(costs) - candidates)
        lh, rh = costs[:left + 1], costs[right:]
        heapq.heapify(lh)
        heapq.heapify(rh)
        ans = 0

        for i in range(k):
            if not rh:
                ans += heapq.heappop(lh)
                continue

            if not lh:
                ans += heapq.heappop(rh)
                continue
            
            if lh[0] <= rh[0]:
                ans += heapq.heappop(lh)
                if left + 1 < right:
                    left += 1
                    heapq.heappush(lh, costs[left])
            else:
                ans += heapq.heappop(rh)
                if right - 1 > left:
                    right -= 1
                    heapq.heappush(rh, costs[right])
        
        return ans