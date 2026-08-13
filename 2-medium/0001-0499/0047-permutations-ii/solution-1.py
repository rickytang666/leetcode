from typing import List
from collections import Counter

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        freqs = Counter(nums)
        def backtrack(arr):
            if len(arr) == n:
                ans.append(arr.copy())
                return
            for num, cnt in freqs.items():
                if cnt > 0:
                    arr.append(num)
                    freqs[num] -= 1
                    backtrack(arr)
                    arr.pop()
                    freqs[num] += 1
        backtrack([])
        return ans