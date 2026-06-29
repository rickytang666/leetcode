from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        d = [
            (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
        ]

        """
        2 -> dead, once alive
        3 -> alive, once dead
        """

        for x in range(m):
            for y in range(n):
                alive = 0
                for dx, dy in d:
                    nx, ny = x + dx, y + dy
                    if nx in range(0, m) and ny in range(0, n) and board[nx][ny] in (1, 2):
                        alive += 1
                if board[x][y] in (1, 2):
                    if alive < 2 or alive > 3:
                        board[x][y] = 2
                else:
                    if alive == 3:
                        board[x][y] = 3
        
        for x in range(m):
            for y in range(n):
                board[x][y] %= 2