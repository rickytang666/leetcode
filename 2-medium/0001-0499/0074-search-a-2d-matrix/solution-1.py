from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target < matrix[0][0] or target > matrix[-1][-1]: return False

        l, h = 0, len(matrix) - 1

        row = -1

        while l <= h:
            m = (l + h) // 2
            if target < matrix[m][0]: h = m -1
            elif target > matrix[m][-1]: l = m + 1
            else: 
                row = m
                break
        
        row = m
        l, h = 0, len(matrix[0]) - 1

        while l <= h:
            m = (l + h) // 2
            if target == matrix[row][m]: return True
            elif target < matrix[row][m]: h = m - 1
            else: l = m + 1
        return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(Solution().searchMatrix(matrix, target))