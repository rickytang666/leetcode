from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = [-1]
        ans = 0

        for i in range(len(heights)):
            while st[-1] != -1 and heights[i] <= heights[st[-1]]:
                height = heights[st.pop()]
                width = i - st[-1] - 1
                ans = max(ans, height * width)
            st.append(i)
        
        while st[-1] != -1 and heights[i] <= heights[st[-1]]:
            height = heights[st.pop()]
            width = len(heights) - st[-1] - 1
            ans = max(ans, height * width)

        return ans
    
heights = [2,1,5,6,2,3]
print(Solution().largestRectangleArea(heights))