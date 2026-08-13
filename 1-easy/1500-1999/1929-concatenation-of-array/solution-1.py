from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        return [nums[i % n] for i in range(n * 2)]