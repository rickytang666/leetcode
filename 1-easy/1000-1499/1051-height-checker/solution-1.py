from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum(h1 != h2 for h1, h2 in zip(heights, sorted(heights)))
    
print(Solution().heightChecker([1,1,4,2,1,3]))  # expected output: 3