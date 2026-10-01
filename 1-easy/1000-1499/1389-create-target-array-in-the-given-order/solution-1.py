from typing import List

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        ans = []
        for x, i in zip(nums, index):
            ans.insert(i, x)
        return ans