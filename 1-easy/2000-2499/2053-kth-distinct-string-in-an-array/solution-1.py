from typing import List

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        mp = {}
        for s in arr:
            if s not in mp:
                mp[s] = 1
            else:
                mp[s] += 1
        
        for s in arr:
            if mp[s] == 1: 
                k -= 1
                if k == 0:
                    return s
            
        return ""