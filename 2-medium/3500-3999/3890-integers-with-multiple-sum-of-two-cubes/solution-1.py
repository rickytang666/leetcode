from collections import defaultdict

class Solution:
    def findGoodIntegers(self, n: int) -> list[int]:
        counts = defaultdict(int)
        a = 1
        while 2 * a**3 <= n:
            b = a
            while a**3 + b**3 <= n:
                counts[a**3 + b**3] += 1
                b += 1
            a += 1
        return sorted(x for x, c in counts.items() if c >= 2)
