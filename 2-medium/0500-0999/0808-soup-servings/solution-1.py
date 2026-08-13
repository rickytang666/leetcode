from math import ceil

class Solution:
    def soupServings(self, n: int) -> float:
        if n >= 5000: return 1
        
        cache = {}
        def P(a, b):
            if (a, b) in cache: return cache[(a, b)]

            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1
            if b <= 0:
                return 0
            
            ans = 0.25 * (
                P(a - 4, b) + 
                P(a - 3, b - 1) + 
                P(a - 2, b - 2) + 
                P(a - 1, b - 3)
            )

            cache[(a, b)] = ans
            return ans
        
        m = ceil(n / 25)
        return P(m, m)