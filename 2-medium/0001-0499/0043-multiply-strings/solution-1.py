class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"
        m, n = len(num1), len(num2)
        ans = [0] * (m + n)
        num1, num2 = num1[::-1], num2[::-1]
        for i in range(m):
            for j in range(n):
                digit = int(num1[i]) * int(num2[j])
                ans[i + j] += digit
                ans[i + j + 1] += (ans[i + j] // 10)
                ans[i + j] %= 10
        
        # leading 0s
        ans, beg = ans[::-1], 0
        while beg < len(ans) and ans[beg] == 0:
            beg += 1
        
        ans = map(str, ans[beg:])

        return "".join(ans)