from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        m = {}
        ans = 0
        for n in nums:
            m[n] = m.get(n, 0) + 1
        for key, val in m.items():
            ans += val * (val - 1) // 2
        return ans