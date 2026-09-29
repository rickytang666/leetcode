from typing import List

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans = []
        i, j = 0, 0
        while i < len(firstList) and j < len(secondList):
            s1, e1 = firstList[i]
            s2, e2 = secondList[j]
            lo = max(s1, s2)
            hi = min(e1, e2)
            if lo <= hi:
                ans.append([lo, hi])
            if e1 < e2:
                i += 1
            else:
                j += 1
        return ans