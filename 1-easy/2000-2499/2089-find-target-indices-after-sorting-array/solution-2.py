from typing import List

# dark magic solution 😱 O(n) 

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        l_cnt, eq_cnt = 0, 0
        for n in nums:
            if n < target: l_cnt += 1
            elif n == target: eq_cnt += 1
        return list(range(l_cnt, l_cnt + eq_cnt))