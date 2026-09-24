from typing import List

class Solution:
    def validStrings(self, n: int) -> List[str]:
        res = ["0", "1"]
        for _ in range(n - 1):
            res = [s + c for s in res for c in "01" if s[-1] == "1" or c == "1"]
        return res