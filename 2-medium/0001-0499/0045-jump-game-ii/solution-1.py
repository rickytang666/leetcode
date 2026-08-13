from typing import List

# greedy BFS

class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = 0
        l = r = 0

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            ans += 1
        
        return ans