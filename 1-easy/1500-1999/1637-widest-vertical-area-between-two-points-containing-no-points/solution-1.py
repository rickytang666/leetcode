from typing import List
from itertools import pairwise

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        xs = sorted(x for x, _ in points)
        return max(b - a for a, b in pairwise(xs))