class Solution:
    def myPow(self, x: float, n: int) -> float:
        def rec(x, n):
            if n == 0:
                return 1
            if n == 1:
                return x
            half = rec(x, n // 2)
            if n % 2:
                return half * half * x
            else:
                return half * half
        
        res = rec(x, abs(n))
        return res if n >= 0 else 1/res
