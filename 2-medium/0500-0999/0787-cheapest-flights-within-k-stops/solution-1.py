from typing import List
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, w in flights:
            adj[u].append((v, w))
        dist = [[float('inf')] * (k + 2) for _ in range(n)]
        dist[src][0] = 0
        pq = [(0, src, 0)]
        while pq:
            cost, node, edges = heapq.heappop(pq)
            if node == dst: return cost
            if edges == k + 1: continue
            for nei, w in adj[node]:
                new_cost = cost + w
                if new_cost < dist[nei][edges + 1]:
                    dist[nei][edges + 1] = new_cost
                    heapq.heappush(pq, (new_cost, nei, edges + 1))
        return -1