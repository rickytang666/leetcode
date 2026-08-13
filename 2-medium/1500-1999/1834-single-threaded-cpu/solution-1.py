from typing import List
import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        available = []
        pending = []
        for i, (enqueTime, processTime) in enumerate(tasks):
            heapq.heappush(pending, (enqueTime, processTime, i))
        time = 0
        ans = []
        while pending or available:
            while pending and pending[0][0] <= time:
                enqueTime, processTime, i = heapq.heappop(pending)
                heapq.heappush(available, (processTime, i))
            if not available:
                time = pending[0][0]
                continue
            processTime, i = heapq.heappop(available)
            time += processTime
            ans.append(i)
        return ans