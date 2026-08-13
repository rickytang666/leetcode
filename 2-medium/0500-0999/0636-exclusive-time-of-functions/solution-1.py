from typing import List

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans = [0] * n
        st = []
        prev = 0
        
        for l in logs:
            id, sig, time = l.split(':')
            id = int(id)
            time = int(time)
            
            if sig == 'start':
                if st:
                    ans[st[-1]] += time - prev
                st.append(id)
                prev = time
            else:
                ans[st.pop()] += time - prev + 1
                prev = time + 1
        
        return ans