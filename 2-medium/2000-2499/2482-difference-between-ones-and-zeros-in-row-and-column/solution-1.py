from typing import List

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        rows = [sum(r) for r in grid]
        cols = [sum(c) for c in zip(*grid)]
        return [[2 * rows[i] + 2 * cols[j] - m - n for j in range(n)] for i in range(m)]