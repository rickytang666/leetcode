from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        target = len(nums) // 3
        can1 = can2 = None
        vote1 = vote2 = 0
        
        for num in nums:
            if num == can1:
                vote1 += 1
            elif num == can2:
                vote2 += 1
            elif vote1 == 0:
                can1, vote1 = num, 1
            elif vote2 == 0:
                can2, vote2 = num, 1
            else:
                vote1 -= 1
                vote2 -= 1
        
        ans = []
        for c in [can1, can2]:
            if c is not None and nums.count(c) > target:
                ans.append(c)
        
        return ans