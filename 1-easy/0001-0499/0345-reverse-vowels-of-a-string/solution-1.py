from typing import*

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        chars = list(s)
        left, right = 0, len(s) - 1

        while left < right:
            if chars[left] not in vowels:
                left += 1
                continue
            if chars[right] not in vowels:
                right -= 1
                continue

            # swap vowels
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
        
        return ''.join(chars)
