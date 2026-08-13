from collections import Counter

#
# @lc app=leetcode id=3541 lang=python3
#
# [3541] Find Most Frequent Vowel and Consonant
#

# @lc code=start
class Solution:
    def maxFreqSum(self, s: str) -> int:
        mp = Counter(s)
        # generator expression is more efficient
        vowel_max = max((mp[c] for c in mp if c in "aeiou"), default=0)
        consonant_max = max((mp[c] for c in mp if c not in "aeiou"), default=0)
        return vowel_max + consonant_max
# @lc code=end

