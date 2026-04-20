from typing import List

# use bit manipulation to achieve constant space
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        for i in range(m):
            for j in range(n):
                sum = count = 0
                for x in range(i - 1, i + 2):
                    for y in range(j - 1, j + 2):
                        if 0 <= x < m and 0 <= y < n:
                            sum += img[x][y] & 255 # extract the original value only (disregard upper bits)
                            count += 1
                img[i][j] |= (sum // count) << 8
        for i in range(m):
            for j in range(n):
                img[i][j] >>= 8
        return img