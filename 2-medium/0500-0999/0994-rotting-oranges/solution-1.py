from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()
        fresh_cnt = 0
        time = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh_cnt += 1

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while fresh_cnt > 0 and q:
            length = len(q)
            for i in range(length):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row in range(m)) and (col in range(n)) and grid[row][col] == 1:
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh_cnt -= 1
            time += 1
        return time if fresh_cnt == 0 else -1