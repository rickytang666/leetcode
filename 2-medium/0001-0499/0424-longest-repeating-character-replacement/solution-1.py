class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_freq = 0
        left = 0
        ans = 0
        
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_freq = max(max_freq, count[s[right]])
            
            # shrink if invalid
            window_size = right - left + 1
            if window_size - max_freq > k:
                count[s[left]] -= 1
                left += 1
            
            ans = max(ans, right - left + 1)
        
        return ans
    
s = "AABABBA"
k = 1
print(Solution().characterReplacement(s, k))