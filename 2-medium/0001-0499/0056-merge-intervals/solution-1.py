from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        start, end = intervals[0]
        ans = []
        for i in range(1, len(intervals)):
            if intervals[i][0] <= end:
                end = max(end, intervals[i][1])
            else:
                ans.append([start, end])
                start, end = intervals[i]
        # flush
        ans.append([start, end])
        return ans