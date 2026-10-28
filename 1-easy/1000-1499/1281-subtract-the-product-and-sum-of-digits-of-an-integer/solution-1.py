class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        p, s = 1, 0
        while n:
            d = n % 10
            p *= d
            s += d
            n //= 10
        return p - s