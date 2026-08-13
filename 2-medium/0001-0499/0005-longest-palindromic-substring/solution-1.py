
class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        ansL = 0
        n = len(s)

        for i in range(n):
            l = r = i
            while l >= 0 and r < n and s[l] == s[r]:
                if (r - l + 1) > ansL:
                    ans = s[l:r+1]
                    ansL = r - l + 1
                l -= 1
                r += 1

            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                if (r - l + 1) > ansL:
                    ans = s[l:r+1]
                    ansL = r - l + 1
                l -= 1
                r += 1

        return ans