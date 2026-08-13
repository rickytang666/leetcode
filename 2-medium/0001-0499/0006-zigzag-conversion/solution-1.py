class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        ans = [[] for _ in range(numRows)]
        i, step = 0, 1

        for char in s:
            ans[i].append(char)

            if i == 0:
                step = 1
            elif i == numRows - 1:
                step = -1
            
            i += step
        
        return ''.join(''.join(a) for a in ans)