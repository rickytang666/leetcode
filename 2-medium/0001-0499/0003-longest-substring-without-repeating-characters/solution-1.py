class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 1: return n
        ans = 0
        arr = [-1] * 128
        l = 0
        for r in range(n):
            # if repeated, move left pointer to the position after the last occurence of that char
            # use ord() to convert to ascii
            if arr[ord(s[r])] >= l:
                l = arr[ord(s[r])] + 1
            arr[ord(s[r])] = r
            ans = max(ans, r - l + 1)
        return ans