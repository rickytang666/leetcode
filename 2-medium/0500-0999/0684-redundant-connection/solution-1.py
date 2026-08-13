from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = {i:[] for i in range(n + 1)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        seen = set()
        cycle = set()
        start = -1

        # pretty confusing dfs
        def dfs(node, parent):
            nonlocal start
            if node in seen:
                start = node
                return True
            
            seen.add(node)
            for nei in adj[node]:
                if nei == parent:
                    continue
                if dfs(nei, node):
                    if start != -1:
                        cycle.add(node)
                    if node == start: # we're back, stop collecting
                        start = -1
                    return True
            return False
        
        dfs(1, -1)
        
        for u, v in reversed(edges):
            if u in cycle and v in cycle:
                return [u, v]
        
        return []