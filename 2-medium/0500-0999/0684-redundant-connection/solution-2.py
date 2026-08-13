from typing import List
from collections import deque

# topological trimming

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = {i:[] for i in range(n + 1)}
        indegree = [0] * (n + 1)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            indegree[u] += 1
            indegree[v] += 1
        
        q = deque()
        for node in range(1, n + 1):
            if indegree[node] == 1:
                q.append(node)
        
        while q:
            node = q.popleft()
            for nei in adj[node]:
                indegree[nei] -= 1
                indegree[node] -= 1
                if indegree[nei] == 1:
                    q.append(nei)
        
        for u, v in reversed(edges):
            if indegree[u] > 0 and indegree[v] > 0:
                return [u, v]
            
        return []