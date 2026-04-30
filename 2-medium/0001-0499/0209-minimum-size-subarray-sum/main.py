from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = total = 0
        n = len(nums)
        ans = n + 1
        for r in range(n):
            total += nums[r]
            while total >= target:
                ans = min(ans, r - l + 1)
                total -= nums[l]
                l += 1
        return 0 if ans == n + 1 else ans