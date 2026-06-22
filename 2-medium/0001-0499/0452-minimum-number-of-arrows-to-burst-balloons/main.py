from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        lastEnd = float('-inf')
        ans = 0

        for start, end in points:
            if start > lastEnd:
                ans += 1
                lastEnd = end
            else:
                lastEnd = min(lastEnd, end)
        
        return ans