#
# @lc app=leetcode id=165 lang=python3
#
# [165] Compare Version Numbers
#

# @lc code=start
from itertools import zip_longest

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # python int() ignores leading zeroes
        v1, v2 = list(map(int, version1.split('.'))), list(map(int, version2.split('.')))
        for rev1, rev2 in zip_longest(v1, v2, fillvalue=0):
            if rev1 < rev2: return -1
            elif rev1 > rev2: return 1
        return 0
        
# @lc code=end

