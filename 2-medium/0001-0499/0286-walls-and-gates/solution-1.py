from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid or not grid[0]:
            return
        m, n = len(grid), len(grid[0])
        INF = 2147483647
        q = deque()

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    q.append((r, c))

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == INF:
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr, nc))