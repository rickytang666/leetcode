from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            sum = 0
            for x in nums:
                sum += (x >> i) & 1
            if sum % 3 != 0:
                ans |= 1 << i
        if ans >= 2**31:
            ans -= 2**32
        return ans