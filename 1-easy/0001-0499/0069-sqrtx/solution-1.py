class Solution:
    def mySqrt(self, x: int) -> int:
        ans = 0
        l, r = 0, x

        while l <= r:
            m = l + (r - l) // 2
            if m * m > x:
                r = m - 1
            elif m * m < x:
                l = m + 1
                ans = m
            else:
                return m
        
        return ans