from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]
        
        n = len(nums)
        lo, mid, hi = 0, 0, n - 1
        while mid <= hi:
            if nums[mid] == 0:
                swap(lo, mid)
                lo += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                swap(mid, hi)
                hi -= 1