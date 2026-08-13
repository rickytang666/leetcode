from typing import*

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1: return ""
        def euclidean_gcd(a, b):
            if a > b:
                a, b = b, a
            while b:
                a, b = b, a % b
            return a
        return str1[:euclidean_gcd(len(str1), len(str2))]
 

str1 = "ABCDEF"
str2 = "ABC"
print(Solution().gcdOfStrings(str1, str2))