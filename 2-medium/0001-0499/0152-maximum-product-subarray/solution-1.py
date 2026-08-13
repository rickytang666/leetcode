from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        currMax = currMin = 1

        for num in nums:
            tmp = currMax * num
            currMax = max(num, currMax * num, currMin * num)
            currMin = min(num, tmp, currMin * num)
            ans = max(ans, currMax)
            
        return ans