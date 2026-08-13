from typing import List

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftSum, rightSum = 0, sum(nums)
        ans = []
        for i in range(len(nums)):
            if i > 0:
                leftSum += nums[i - 1]
            rightSum -= nums[i]
            ans.append(abs(leftSum - rightSum))
        return ans