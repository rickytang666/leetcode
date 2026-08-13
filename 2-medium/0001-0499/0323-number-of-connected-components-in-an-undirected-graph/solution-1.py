from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        seen = set()
        
        def dfs(node):
            for nei in adj[node]:
                if nei not in seen:
                    seen.add(nei)
                    dfs(nei)
        
        ans = 0
        for node in range(n):
            if node not in seen:
                seen.add(node)
                dfs(node)
                ans += 1
        
        return ans