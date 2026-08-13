from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        l, r = 0, n - 1
        while l < r:
            mid = l + (r - l) // 2
            if x > arr[mid]:
                l = mid + 1
            else:
                r = mid
        l, r = l - 1, l
        while r - l - 1 < k:
            if l < 0:
                r += 1
            elif r >= n:
                l -= 1
            elif abs(arr[l] - x) <= abs(arr[r] - x):
                l -= 1
            else:
                r += 1
        return arr[l + 1:r]