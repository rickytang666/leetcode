from typing import List

# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(n, r, c):
            if n == 1:
                return Node(grid[r][c], True)
            mid = n // 2
            tl = dfs(mid, r, c)
            tr = dfs(mid, r, c + mid)
            bl = dfs(mid, r + mid, c)
            br = dfs(mid, r + mid, c + mid)
            if (tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf) and (tl.val == tr.val == bl.val == br.val):
                return Node(tl.val, True)
            return Node(False, False, tl, tr, bl, br)
        return dfs(len(grid), 0, 0)