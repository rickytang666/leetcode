from typing import List

class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        def find_x(reverse):
            if reverse:
                for j in range(len(grid[0]) - 1, -1, -1):
                    for i in range(len(grid)):
                        if grid[i][j]: return j
            else:
                for j in range(len(grid[0])):
                    for i in range(len(grid)):
                        if grid[i][j]: return j
        def find_y(reverse):
            if reverse:
                for i in range(len(grid) - 1, -1, -1):
                    for j in range(len(grid[0])):
                        if grid[i][j]: return i
            else:
                for i in range(len(grid)):
                    for j in range(len(grid[0])):
                        if grid[i][j]: return i
        
        top, btm, left, right = find_y(False), find_y(True), find_x(False), find_x(True)
        
        return (btm - top + 1) * (right - left + 1)
                        