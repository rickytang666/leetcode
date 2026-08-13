from typing import List

class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        s = sum(nums)
        l, r = 0, s

        for i in range(n):
            if nums[i] == 0:
                if 0 <= l - r <= 1:
                    ans += 1
                if 0 <= r - l <= 1:
                    ans += 1
            else:
                l += nums[i]
                r -= nums[i]
        
        return ans