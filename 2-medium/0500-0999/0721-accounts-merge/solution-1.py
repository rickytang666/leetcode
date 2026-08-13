from typing import List
from collections import defaultdict

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, a, b):
        pa, pb = self.find(a), self.find(b)
        if pa == pb:
            return False
        if self.size[pa] < self.size[pb]:
            pa, pb = pb, pa
        self.parent[pb] = pa
        self.size[pa] = self.size[pb]
        return True
    
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = DSU(len(accounts))
        emailToAcc = {}

        for i, arr in enumerate(accounts):
            for e in arr[1:]:
                if e in emailToAcc:
                    uf.union(i, emailToAcc[e])
                else:
                    emailToAcc[e] = i
        
        emailGroup = defaultdict(list)

        for e, i in emailToAcc.items():
            emailGroup[uf.find(i)].append(e)
        
        ans = []
        for i, arr in emailGroup.items():
            name = accounts[i][0]
            ans.append([name] + sorted(arr))
        
        return ans