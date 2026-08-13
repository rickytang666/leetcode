#
# @lc app=leetcode id=1221 lang=python3
#
# [1221] Split a String in Balanced Strings
#

# @lc code=start
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balance = 0
        ans = 0
        for c in s:
            if c == 'L': balance += 1
            else: balance -= 1
            if balance == 0: ans += 1

        return ans
        
# @lc code=end

