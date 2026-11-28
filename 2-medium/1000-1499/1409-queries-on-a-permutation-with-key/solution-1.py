from typing import List

class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        p = list(range(1, m + 1))
        ans = []
        for q in queries:
            i = p.index(q)
            ans.append(i)
            p.insert(0, p.pop(i))
        return ans