class Solution:
    def countAsterisks(self, s: str) -> int:
        ans = 0
        bar_cnt = 0
        for c in s:
            if c == '|':
                bar_cnt ^= 1
            if c == '*' and bar_cnt == 0:
                ans += 1
        return ans