from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans = 0
        rows, cols = len(strs), len(strs[0])
        for c in range(cols):
            for r in range(1, rows):
                if ord(strs[r][c]) < ord(strs[r - 1][c]):
                    ans += 1
                    break
        return ans