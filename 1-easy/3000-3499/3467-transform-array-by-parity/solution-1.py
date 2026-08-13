from typing import List

class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        odd = 0
        for n in nums:
            if n % 2: odd += 1
        even = len(nums) - odd
        return [0] * even + [1] * odd