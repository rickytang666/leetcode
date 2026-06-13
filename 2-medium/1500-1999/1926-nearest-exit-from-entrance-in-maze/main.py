from typing import List
from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        q = deque()
        moves = 1
        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        q.append(entrance)
        maze[entrance[0]][entrance[1]] = '+'

        while q:
            l = len(q)
            for i in range(l):
                x, y = q.popleft()
                for dx, dy in directions:
                    newX, newY = x + dx, y + dy
                    if newX not in range(0, m) or newY not in range(0, n) or maze[newX][newY] == '+':
                        continue
                    if newX == 0 or newY == 0 or newX == m - 1 or newY == n - 1:
                        return moves
                    maze[newX][newY] = '+'
                    q.append([newX, newY])
            
            moves += 1
        
        return -1