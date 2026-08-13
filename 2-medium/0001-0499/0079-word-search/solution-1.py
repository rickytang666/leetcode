from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(word)
        rows, cols = len(board), len(board[0])
        def dfs(r, c, i):
            if i == n: return True
            if r < 0 or r >= rows or c < 0 or c >= cols: return False
            if board[r][c] != word[i]: return False
            temp = board[r][c]
            board[r][c] = '#'

            found = dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1)

            board[r][c] = temp
            return found
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0): return True
        return False