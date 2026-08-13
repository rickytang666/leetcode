#
# @lc app=leetcode id=3280 lang=python3
#
# [3280] Convert Date to Binary
#

# @lc code=start
class Solution:
    def convertDateToBinary(self, date: str) -> str:
        nums = date.split('-')
        ans = []
        for num in nums:
            ans.append(bin(int(num))[2:])
        return '-'.join(ans)
# @lc code=end

