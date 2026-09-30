class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        l = len(word)
        n = len(sequence)
        dp = [0] * (n + 1)
        for i in range(l, n + 1):
            if sequence[i - l:i] == word:
                dp[i] = dp[i - l] + 1
        return max(dp)