from typing import*

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_v = max(candies)
        return [n + extraCandies >= max_v for n in candies]
    
candies = [2, 3, 5, 1, 3]
extraCandies = 3
print(Solution().kidsWithCandies(candies, extraCandies))