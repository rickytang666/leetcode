from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        
        def backtrack(pos, curr):
            nonlocal ans
            if pos == n:
                ans += curr
                return
            
            backtrack(pos + 1, curr)
            backtrack(pos + 1, curr ^ nums[pos])
        
        backtrack(0, 0)
        return ans