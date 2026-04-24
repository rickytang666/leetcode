from typing import List
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        target = len(nums) // 3
        m = Counter(nums)
        return [num for num in m if m[num] > target]