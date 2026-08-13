class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        def rev(n):
            ans = 0
            while n > 0:
                ans = ans * 10 + n % 10
                n //= 10
            return ans
        return rev(rev(num)) == num