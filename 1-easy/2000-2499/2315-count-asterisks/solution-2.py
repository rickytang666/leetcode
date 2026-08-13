class Solution:
    def countAsterisks(self, s: str) -> int:
        arr = s.split('|')
        return sum(arr[i].count('*') for i in range(0, len(arr), 2))