from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        ans = [""] * n
        sorted_scores = sorted([(s, i) for i, s in enumerate(score)], reverse=True)
        for rank, (s, i) in enumerate(sorted_scores):
            if rank == 0:
                ans[i] = "Gold Medal"
            elif rank == 1:
                ans[i] = "Silver Medal"
            elif rank == 2:
                ans[i] = "Bronze Medal"
            else:
                ans[i] = str(rank + 1)
        return ans