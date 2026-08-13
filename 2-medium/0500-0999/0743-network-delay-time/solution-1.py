from collections import defaultdict
from typing import List
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        q = [(0, k)]
        visited = set()

        ans = 0

        while q:
            w1, n1 = heapq.heappop(q)
            if n1 in visited:
                continue
            visited.add(n1)
            ans = w1

            for n2, w2 in graph[n1]:
                if n2 not in visited:
                    heapq.heappush(q, (w1 + w2, n2))
        
        return ans if len(visited) == n else -1