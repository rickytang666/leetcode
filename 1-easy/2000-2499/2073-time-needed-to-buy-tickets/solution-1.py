from typing import List

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0
        for i in range(len(tickets)):
            ans += min(tickets[i], tickets[k]) if i <= k else min(tickets[i], tickets[k] - 1)
        return ans