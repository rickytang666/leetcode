from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prevH):
            if r < 0 or c < 0 or r == m or c == n or (r, c) in visit or heights[r][c] < prevH: return

            visit.add((r, c))

            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        for c in range(n):
            dfs(0, c, pac, 0)
            dfs(m - 1, c, atl, 0)
        
        for r in range(m):
            dfs(r, 0, pac, 0)
            dfs(r, n - 1, atl, 0)

        ans = []

        for r in range(m):
            for c in range(n):
                if (r, c) in pac and (r, c) in atl:
                    ans.append([r, c])

        return ans