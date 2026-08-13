class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = ""
        start = 0
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(s[i])
            elif stack[-1] == '(':
                stack.pop()
            
            if not stack:
                ans += s[start+1:i]
                start = i + 1

        return ans