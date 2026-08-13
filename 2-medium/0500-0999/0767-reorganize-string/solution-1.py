from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        maxHeap = [[-cnt, char] for char, cnt in Counter(s).items()]
        heapq.heapify(maxHeap)

        prev = None
        ans = ""

        while prev or maxHeap:
            if prev and not maxHeap:
                return ""
            cnt, char = heapq.heappop(maxHeap)
            ans += char
            cnt += 1
            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            if cnt != 0:
                prev = [cnt, char]
        
        return ans