from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums) - 2):
            c, a, b = nums[i], nums[i + 1], nums[i + 2]
            if a + b > c:
                return a + b + c
        return 0