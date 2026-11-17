from typing import List

class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ans = []
        for cx, cy, r in queries:
            cnt = 0
            for x, y in points:
                if (x - cx) ** 2 + (y - cy) ** 2 <= r ** 2:
                    cnt += 1
            ans.append(cnt)
        return ans