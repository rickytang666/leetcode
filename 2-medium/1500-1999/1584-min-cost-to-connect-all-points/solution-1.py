from typing import List
import heapq

# prim's algorithm

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = {i:[] for i in range(n)}
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        
        ans = 0
        visited = set()
        min_h = [[0, 0]]

        while min_h:
            weight, u = heapq.heappop(min_h)

            if u in visited:
                continue

            visited.add(u)
            ans += weight

            for w, v in adj[u]:
                if v not in visited:
                    heapq.heappush(min_h, [w, v])
            
        return ans