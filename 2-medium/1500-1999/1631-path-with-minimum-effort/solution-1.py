from typing import List
import heapq

# dijkstra

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        q = [[0, 0, 0]]
        visited = set()

        while q:
            diff, r, c = heapq.heappop(q)
            if (r, c) in visited: continue
            visited.add((r, c))
            if (r, c) == (m-1, n-1): return diff
            for dr, dc in directions:
                newR, newC = r + dr, c + dc
                if newR not in range(0, m) or newC not in range(0, n) or (newR, newC) in visited: continue
                newDiff = max(diff, abs(heights[r][c] - heights[newR][newC]))
                heapq.heappush(q, [newDiff, newR, newC])

        return 0