from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)

        for h in range(1, len(citations) + 1):
            if citations[h - 1] < h:
                return h - 1
        
        return len(citations)