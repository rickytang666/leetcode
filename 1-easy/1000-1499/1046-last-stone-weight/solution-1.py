from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        q = [-x for x in stones]
        heapq.heapify(q)
        while len(q) > 1:
            x = heapq.heappop(q)
            y = heapq.heappop(q)
            if y > x:
                heapq.heappush(q, x - y)
        q.append(0)
        return abs(q[0])