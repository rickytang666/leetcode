class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        k = n // m
        num2 = m * k * (k + 1) // 2
        total = n * (n + 1) // 2
        return total - num2 * 2