from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        lo, hi = 0, n - 1
        while lo <= hi:
            m = lo + (hi - lo) // 2
            if nums[m] == target: return True
            
            if nums[lo] < nums[m]:
                if nums[lo] <= target < nums[m]:
                    hi = m - 1
                else:
                    lo = m + 1
            elif nums[lo] > nums[m]:
                if nums[m] < target <= nums[hi]:
                    lo = m + 1
                else:
                    hi = m - 1
            else:
                lo += 1
        return False