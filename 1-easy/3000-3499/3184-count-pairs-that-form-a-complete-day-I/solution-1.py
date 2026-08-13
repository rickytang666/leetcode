from collections import defaultdict
from typing import List

class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        remainders = defaultdict(int)
        cnt = 0
        for h in hours:
            rem = h % 24
            if rem == 0:
                cnt += remainders[0]
            else:
                cnt += remainders[24 - rem]
            remainders[rem] += 1
        return cnt