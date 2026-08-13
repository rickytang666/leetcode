from typing import List
from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        inbound = defaultdict(int)
        outbound = defaultdict(int)

        for a, b in trust:
            outbound[a] += 1
            inbound[b] += 1
        
        for i in range(1, n + 1):
            if inbound[i] == n - 1 and outbound[i] == 0:
                return i
        
        return -1