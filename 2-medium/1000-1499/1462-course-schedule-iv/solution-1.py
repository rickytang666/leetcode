from typing import List

# dfs with memo

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [[] for _ in range(numCourses)]
        memo = [[-1] * numCourses for _ in range(numCourses)]

        for p, c in prerequisites:
            adj[c].append(p)
            memo[c][p] = 1

        def dfs(course, prerequisite):
            if memo[course][prerequisite] != -1:
                return memo[course][prerequisite] == 1
            for p in adj[course]:
                if p == prerequisite or dfs(p, prerequisite):
                    memo[course][prerequisite] = 1
                    return True
            memo[course][prerequisite] = 0
            return False
        
        return [dfs(v, u) for u, v in queries]