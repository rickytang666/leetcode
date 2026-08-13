from typing import List

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        l, r, ans, prev = 0, 1, 1, ""

        while r < n:
            if arr[r - 1] > arr[r] and prev != ">":
                ans = max(ans, r - l + 1)
                r += 1
                prev = ">"
            elif arr[r - 1] < arr[r] and prev != "<":
                ans = max(ans, r - l + 1)
                r += 1
                prev = "<"
            else:
                if arr[r] == arr[r - 1]:
                    r += 1
                l = r - 1
                prev = ""
        
        return ans