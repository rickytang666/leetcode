from typing import List

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0: return False
        sideLength = total // 4
        matchsticks.sort(reverse=True)
        sides = [0, 0, 0, 0]
        def dfs(i):
            if i == len(matchsticks):
                return True
            for side in range(4):
                if side > 0 and sides[side] == sides[side - 1]:
                    continue
                if sides[side] + matchsticks[i] <= sideLength:
                    sides[side] += matchsticks[i]
                    if dfs(i + 1):
                        return True
                    sides[side] -= matchsticks[i]
            return False
        return dfs(0)