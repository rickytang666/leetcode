from typing import List
from heapq import heappush, heappop
from itertools import pairwise

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        for i, (a, b) in enumerate(pairwise(heights)):
            d = b - a
            if d > 0:
                heappush(heap, d)
                if len(heap) > ladders:
                    bricks -= heappop(heap)
                    if bricks < 0:
                        return i
        return len(heights) - 1