from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.ans = []

        def backtrack(path, total, largest):
            if largest > 9:
                return
            if len(path) == k:
                if total == n:
                    self.ans.append(path)
                return
            if total >= n:
                return
            
            for i in range(largest + 1, 10):
                backtrack(path + [i], total + i, i)
        
        backtrack([], 0, 0)
        return self.ans