from typing import List

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = prices
        st = []
        for i in range(len(prices)):
            while st and prices[i] <= prices[st[-1]]:
                ans[st.pop()] -= prices[i]
            st.append(i)
        return ans