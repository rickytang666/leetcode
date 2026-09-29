from typing import List
from collections import Counter

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        first, last = {}, {}
        for i, x in enumerate(nums):
            first.setdefault(x, i)
            last[x] = i

        count = Counter(nums)
        degree = max(count.values())
        return min(last[x] - first[x] + 1 for x in count if count[x] == degree)