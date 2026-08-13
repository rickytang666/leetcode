from typing import List

#
# @lc app=leetcode id=1684 lang=python3
#
# [1684] Count the Number of Consistent Strings
#

# @lc code=start
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        char_set = set(allowed)
        def check(word):
            for c in word:
                if not (c in allowed): return False
            return True
        ans = 0
        for word in words:
            if check(word): ans += 1
        return ans
# @lc code=end

