class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        divisor = 5

        while n >= divisor:
            ans += n // divisor
            divisor *= 5
        
        return ans