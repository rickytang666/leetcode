from typing import*

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(current, open_cnt, close_cnt):
            if open_cnt == n and close_cnt == n:
                ans.append(current)
                return

            if open_cnt < n:
                backtrack(current + '(', open_cnt + 1, close_cnt)

            if close_cnt < open_cnt:
                backtrack(current + ')', open_cnt, close_cnt + 1)

        backtrack("", 0, 0)
        return ans 