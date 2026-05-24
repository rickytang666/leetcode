class Solution:
    def integerBreak(self, n: int) -> int:
        memo = {1 : 1}

        def dfs(num):
            if num in memo: return memo[num]
            memo[num] = 0 if num == n else num
            for i in range(1, num):
                memo[num] = max(memo[num], dfs(i) * dfs(num - i))
            return memo[num]
        
        return dfs(n)