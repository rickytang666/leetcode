class Solution:
    def decodeString(self, s: str) -> str:
        currNum = 0
        currStr = ''
        st = []
        for c in s:
            if c == '[':
                # push and reset everything
                st.append(currStr)
                st.append(currNum)
                currStr = ''
                currNum = 0
            elif c == ']':
                freq = st.pop()
                prevStr = st.pop()
                currStr = prevStr + freq * currStr
            elif c.isdigit():
                currNum = currNum * 10 + int(c)
            else:
                currStr += c
        return currStr