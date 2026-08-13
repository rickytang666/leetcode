from typing import List

class Solution:
    def minElement(self, nums: List[int]) -> int:
        def digitSum(n):
            s = 0
            while n:
                s += n % 10
                n //= 10
            return s
        return min(digitSum(n) for n in nums)