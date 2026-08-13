#
# @lc app=leetcode id=1925 lang=python3
#
# [1925] Count Square Sum Triples
#

# @lc code=start
class Solution:
    def countTriples(self, n: int) -> int:
        ans = 0
        sq = {i**2 : i for i in range(1, n + 1)}
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                s = a**2 + b**2
                if s in sq:
                    ans += 1
        return ans
# @lc code=end

