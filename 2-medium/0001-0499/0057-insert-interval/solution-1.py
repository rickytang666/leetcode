from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        added = False
        for i in range(len(intervals)):
            if intervals[i][1] < newInterval[0]:
                ans.append(intervals[i])
            elif intervals[i][0] > newInterval[1]:
                if not added:
                    ans.append(newInterval)
                    added = True
                ans.append(intervals[i])
            else:
                newInterval[0] = min(intervals[i][0], newInterval[0])
                newInterval[1] = max(intervals[i][1], newInterval[1])
        if not added:
            ans.append(newInterval)
        return ans