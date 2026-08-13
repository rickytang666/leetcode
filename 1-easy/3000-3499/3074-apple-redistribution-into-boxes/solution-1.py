from typing import List

class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)
        s = sum(apple)
        pos = 0
        ans = 0
        while s > 0:
            s -= capacity[pos]
            pos += 1
            ans += 1
        return ans