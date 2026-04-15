class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0 or carry:
            dA = int(a[i]) if i >= 0 else 0
            dB = int(b[j]) if j >= 0  else 0
            total = dA + dB + carry
            ans.append(total % 2)
            carry = total // 2
            i -= 1
            j -= 1
        ans.reverse()
        return ''.join(map(str, ans))