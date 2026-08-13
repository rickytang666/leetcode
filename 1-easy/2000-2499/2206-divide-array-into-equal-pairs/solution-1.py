from typing import List
from collections import defaultdict

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        mp = defaultdict(int)
        for num in nums:
            mp[num] += 1
        for cnt in mp.values():
            if cnt % 2 == 1:
                return False
        return True