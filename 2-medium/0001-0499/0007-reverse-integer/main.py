class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX, INT_MIN = 2**31 - 1, -2 ** 31
        ans = 0
        while x:
            digit = int(x % 10) if x >= 0 else int(x % (-10))
            x = (x - digit) // 10

            if ans > INT_MAX // 10 or (ans == INT_MAX // 10 and digit > INT_MAX % 10) or ans <= INT_MIN // 10 or (ans == INT_MIN // 10 and digit < INT_MIN % 10):
                return 0
            
            ans = ans * 10 + digit
        return ans