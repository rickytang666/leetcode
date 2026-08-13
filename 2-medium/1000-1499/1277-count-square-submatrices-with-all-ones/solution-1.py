from typing import List

# so fricking slow...

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        def valid(a, b, size):
            for i in range(a, a + size):
                for j in range(b, b + size):
                    if not matrix[i][j]: return False
            return True

        ans = 0

        for size in range(1, min(len(matrix), len(matrix[0])) + 1):
            for i in range(len(matrix) - size + 1):
                for j in range(len(matrix[i]) - size + 1):
                    if valid(i, j, size): ans += 1
        
        return ans
    
matrix = [
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]

print(Solution().countSquares(matrix))