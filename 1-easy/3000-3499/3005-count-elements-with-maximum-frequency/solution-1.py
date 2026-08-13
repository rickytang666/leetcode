from typing import List

#
# @lc app=leetcode id=3005 lang=python3
#
# [3005] Count Elements With Maximum Frequency
#

# @lc code=start
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        frequencies = [0] * 101
        ans = 0
        max_freq = 0
        for num in nums:
            frequencies[num] += 1
            if frequencies[num] > max_freq:
                max_freq = frequencies[num]
                ans = max_freq
            elif frequencies[num] == max_freq:
                ans += max_freq
        return ans
        
# @lc code=end

