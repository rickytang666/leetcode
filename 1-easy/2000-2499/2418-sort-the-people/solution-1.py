from typing import List

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        mp = dict(zip(heights, names))
        heights.sort(reverse=True)
        return [mp[h] for h in heights]