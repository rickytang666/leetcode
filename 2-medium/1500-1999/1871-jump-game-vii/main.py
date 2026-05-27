class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[n - 1] == '1': return False

        dp = [False] * n
        dp[0] = True

        j = 0

        for i in range(n):
            if not dp[i]: continue
            j = max(j, i + minJump)
            while j <= min(i + maxJump, n - 1):
                if s[j] == '0': dp[j] = True
                j += 1

        return dp[n - 1]