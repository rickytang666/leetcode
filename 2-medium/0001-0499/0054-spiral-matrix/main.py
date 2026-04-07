from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        ans = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        steps = [n, m - 1]
        r, c, d = 0, -1, 0
        while steps[d & 1]:
            for i in range(steps[d & 1]):
                r += directions[d][0]
                c += directions[d][1]
                ans.append(matrix[r][c])
            steps[d & 1] -= 1
            d += 1
            d %= 4
        return ans