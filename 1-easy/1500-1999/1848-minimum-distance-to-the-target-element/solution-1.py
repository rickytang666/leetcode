from typing import List

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        n = len(nums)
        ans = n
        left, right = 0, n - 1
        while left <= right:
            if nums[left] == target:
                ans = min(ans, abs(left - start))
            if nums[right] == target:
                ans = min(ans, abs(right - start))
            left += 1
            right -= 1
        return ans