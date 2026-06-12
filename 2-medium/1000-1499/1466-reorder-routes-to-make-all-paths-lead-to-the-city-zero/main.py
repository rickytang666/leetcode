from typing import List
from collections import defaultdict

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a, b in connections:
            adj[a].append((b, 1))
            adj[b].append((a, 0))
        
        self.ans = 0

        def dfs(node, parent):
            for nei, cost in adj[node]:
                if nei == parent:
                    continue
                self.ans += cost
                dfs(nei, node)
        
        dfs(0, -1)
        return self.ans