from typing import*

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        st = []

        for i in range(len(temperatures)):
            while st and temperatures[i] > temperatures[st[-1]]:
                index = st.pop()
                ans[index] = i - index
            st.append(i)
        
        return ans