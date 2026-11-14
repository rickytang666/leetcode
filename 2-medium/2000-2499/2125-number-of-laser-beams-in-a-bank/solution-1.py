from typing import List

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev = total = 0
        for row in bank:
            cnt = row.count('1')
            if cnt:
                total += prev * cnt
                prev = cnt
        return total