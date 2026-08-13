from typing import List

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        s = set()
        ans = []
        for n in nums:
            if n in s:
                ans.append(n)
            else:
                s.add(n)
            
            if len(ans) == 2:
                break
        return ans