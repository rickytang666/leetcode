from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for right in asteroids:
            while st and right < 0 and st[-1] > 0:
                offset = st[-1] + right
                if offset > 0:
                    right = 0
                elif offset < 0:
                    st.pop()
                else:
                    right = 0
                    st.pop()
            
            if right:
                st.append(right)

        return st