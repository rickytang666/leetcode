#
# @lc app=leetcode id=2942 lang=python3
#
# [2942] Find Words Containing Character
#

# @lc code=start

from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans = []
        for i, word in enumerate(words):
            if x in word: ans.append(i)
        return ans
        
# @lc code=end

