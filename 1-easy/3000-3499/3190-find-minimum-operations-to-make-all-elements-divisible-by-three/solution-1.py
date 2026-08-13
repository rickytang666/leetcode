from typing import List
#
# @lc app=leetcode id=3190 lang=python3
#
# [3190] Find Minimum Operations to Make All Elements Divisible by Three
#

# @lc code=start
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return sum([num % 3 != 0 for num in nums])
# @lc code=end

