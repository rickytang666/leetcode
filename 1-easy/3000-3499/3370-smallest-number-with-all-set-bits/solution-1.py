class Solution:
    def smallestNumber(self, n: int) -> int:
        x = 2
        while x <= n:
            x *= 2
        return x - 1