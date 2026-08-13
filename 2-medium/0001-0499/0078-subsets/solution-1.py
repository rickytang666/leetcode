from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.path = []

        def backtrack(i):
            if i == len(nums):
                self.ans.append(self.path[:]) # snapshot
                return
            
            self.path.append(nums[i])
            backtrack(i + 1)

            self.path.pop() # undo
            backtrack(i + 1)
        
        backtrack(0)
        return self.ans