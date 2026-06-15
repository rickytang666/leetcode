from typing import List
import heapq

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        h = []
        ans = 0
        total = 0
        for a, b in sorted(list(zip(nums1, nums2)), key=lambda x: -x[1]):
            heapq.heappush(h, a)
            total += a
            if len(h) > k: total -= heapq.heappop(h)
            if len(h) == k: ans = max(ans, total * b)
        return ans
