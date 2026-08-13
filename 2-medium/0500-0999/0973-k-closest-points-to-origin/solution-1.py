from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        q = []
        for x, y in points:
            d = x * x + y * y
            heapq.heappush(q, (-d, [x, y]))
            if len(q) > k: heapq.heappop(q)
        return [p for (_, p) in q]