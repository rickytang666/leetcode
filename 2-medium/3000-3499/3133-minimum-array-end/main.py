class Solution:
    def minEnd(self, n: int, x: int) -> int:
        n -= 1
        ans = x
        bit = 0

        while n:
            if ((x >> bit) & 1) == 0:
                ans |= (n & 1) << bit
                n >>= 1
            bit += 1
        
        return ans