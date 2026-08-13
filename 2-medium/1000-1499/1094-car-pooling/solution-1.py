from typing import List
import heapq

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        h = []
        curr = 0
        for num, start, end in trips:
            while h and h[0][0] <= start:
                dropoff, p = heapq.heappop(h)
                curr -= p
            curr += num
            if curr > capacity: return False
            heapq.heappush(h, (end, num))
        return True