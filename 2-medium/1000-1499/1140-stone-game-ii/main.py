from typing import List

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        memo = {}
        n = len(piles)

        def dfs(alice, i, M):
            if i == n: return 0
            if (alice, i, M) in memo: return memo[(alice, i, M)]
            res = 0 if alice else float('inf')
            total = 0
            for X in range(1, 2 * M + 1):
                if i + X > n: break
                total += piles[i + X - 1]
                if alice:
                    res = max(res, total + dfs(not alice, i + X, max(M, X)))
                else:
                    res = min(res, dfs(not alice, i + X, max(M, X)))
                memo[((alice, i, M))] = res
            return res
        
        return dfs(True, 0, 1)