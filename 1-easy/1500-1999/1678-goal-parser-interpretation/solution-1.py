#
# @lc app=leetcode id=1678 lang=python3
#
# [1678] Goal Parser Interpretation
#

# @lc code=start
class Solution:
    def interpret(self, command: str) -> str:
        i = 0
        ans = []
        while i < len(command):
            if command[i] == 'G':
                ans.append('G')
            elif command[i - 1 : i + 1] == '()':
                ans.append('o')
            elif command[i - 3 : i + 1] == '(al)':
                ans.append('al')
            i += 1
        return ''.join(ans)
# @lc code=end

