from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] == 'X' or board[r][c] == '#':
                return
            board[r][c] = '#'
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)
        
        for c in range(n):
            dfs(0, c)
            dfs(m - 1, c)
        
        for r in range(1, m - 1):
            dfs(r, 0)
            dfs(r, n - 1)

        for r in range(m):
            for c in range(n):
                if board[r][c] == '#':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'