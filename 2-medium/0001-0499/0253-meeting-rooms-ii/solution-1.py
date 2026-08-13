from typing import List
import heapq

# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x:x.start)

        q = [intervals[0].end]
        heapq.heapify(q)

        for i in range(1, len(intervals)):
            if q and intervals[i].start >= q[0]:
                heapq.heappop(q)
            heapq.heappush(q, intervals[i].end)

        return len(q)