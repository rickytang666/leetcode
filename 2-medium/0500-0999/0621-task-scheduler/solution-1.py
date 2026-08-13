from typing import List
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        fMax = max(freq.values())
        k = sum(1 for v in freq.values() if v == fMax)
        return max(
            len(tasks),
            (fMax - 1) * (n + 1) + k
        )