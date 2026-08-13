from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = [0] * 101
        data = [0] * 101
        ans = []
        for n in nums:
            arr[n] += 1
        sum = 0
        for i in range(101):
            data[i] = sum
            sum += arr[i]
        return [data[n] for n in nums]