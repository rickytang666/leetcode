from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        self.visited = [False] * len(rooms)

        def dfs(u):
            self.visited[u] = True
            for v in rooms[u]:
                if not self.visited[v]: dfs(v)
        
        dfs(0)

        for visit in self.visited:
            if not visit:
                return False
        
        return True