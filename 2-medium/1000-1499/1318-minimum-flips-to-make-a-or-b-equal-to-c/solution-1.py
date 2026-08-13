class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0
        while a > 0 or b > 0 or c > 0:
            aa, bb, cc = a & 1, b & 1, c & 1

            if cc == 0:
                ans += aa + bb
            else:
                if aa == 0 and bb == 0:
                    ans += 1

            a >>= 1
            b >>= 1
            c >>= 1
        return ans