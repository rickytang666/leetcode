#
# @lc app=leetcode id=3498 lang=python3
#
# [3498] Reverse Degree of a String
#

# @lc code=start
class Solution:
    def reverseDegree(self, s: str) -> int:
        ord_z = ord('z')
        return sum((ord_z - ord(s[i]) + 1) * (i + 1) for i in range(len(s)))
# @lc code=end

