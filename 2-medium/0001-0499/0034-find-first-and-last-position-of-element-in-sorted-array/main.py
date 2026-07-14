from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        ans = [-1, -1]
        if n == 0: return ans
        low, high = 0, n - 1

        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                ans[0] = mid
                high = mid - 1
        
        low, high = 0, n - 1

        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                ans[1] = mid
                low = mid + 1
        
        return ans