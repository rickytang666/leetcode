from typing import*

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cnt = 0
        total = len(flowerbed)
        for i in range(total):
            if flowerbed[i]: continue
            if i > 0 and flowerbed[i - 1]: continue
            if i < total - 1 and flowerbed[i + 1]: continue
            cnt += 1
            flowerbed[i] = 1
            if cnt >= n: return True
        return cnt >= n
