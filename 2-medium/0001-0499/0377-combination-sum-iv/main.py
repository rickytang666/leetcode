from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        memo = {0 : 1}

        def dfs(total):
            if total in memo: return memo[total]

            ans = 0
            for num in nums:
                if total < num: break
                ans += dfs(total - num)
            memo[total] = ans

            return ans
        
        return dfs(target)