from typing import List

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        m = len(potions)
        ans = []
        for s in spells:
            min_possible = -1
            lo, hi = 0, m - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if s * potions[mid] >= success:
                    min_possible = mid
                    hi = mid - 1
                else:
                    lo = mid + 1
            ans.append(0 if min_possible == -1 else m - min_possible)
        return ans