from typing import List

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        height = [0] * n
        ans = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j]:
                    height[j] += 1
                else:
                    height[j] = 0
            temp = sorted(height.copy(), reverse=True)
            for w in range(1, n + 1):
                ans = max(ans, w * temp[w - 1])
        return ans