from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        m = {i:[] for i in range(numCourses)}
        for course, pre in prerequisites:
            m[course].append(pre)
        
        visiting = set()

        def dfs(c):
            if c in visiting:
                return False
            if m[c] == []:
                return True
            visiting.add(c)
            for p in m[c]:
                if not dfs(p):
                    return False
            visiting.remove(c)
            m[c] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True