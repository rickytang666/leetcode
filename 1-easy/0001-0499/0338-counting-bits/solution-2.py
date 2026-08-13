from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        nearestPow = 1
        for i in range(1, n + 1):
            if nearestPow * 2 == i:
                nearestPow = i
            ans[i] = 1 + ans[i - nearestPow]
        return ans