from typing import List

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        nums_set = set(nums)
        ans = 0
        n = len(nums)
        for i in range(n - 2):
            if (nums[i] + diff) in nums_set and (nums[i] + diff * 2) in nums_set:
                ans += 1
        return ans