from typing import List

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        rootA, rootB = self.find(a), self.find(b)
        if rootA == rootB:
            return False
        if self.size[rootA] < self.size[rootB]:
            rootA, rootB = rootB, rootA
        self.parent[rootB] = rootA
        self.size[rootA] += self.size[rootB]
        return True

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        dsu = DSU(n)
        ans = n
        
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j]:
                    if dsu.union(i, j):
                        ans -= 1
        
        return ans