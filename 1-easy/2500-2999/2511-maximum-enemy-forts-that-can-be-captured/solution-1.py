from typing import List

class Solution:
    def captureForts(self, forts: List[int]) -> int:
        last = -1
        ans = 0

        for i in range(len(forts)):
            if forts[i] != 0:
                if last != -1 and forts[i] != forts[last]:
                    ans = max(ans, i - last - 1)
                last = i
        
        return ans