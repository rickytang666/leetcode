import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        ans = ""
        h = []
        for cnt, c in [(-a, 'a'), (-b, 'b'), (-c, 'c')]:
            if cnt != 0:
                heapq.heappush(h, (cnt, c))
        while h:
            cnt, c = heapq.heappop(h)
            if len(ans) >= 2 and ans[-1] == ans[-2] == c:
                if not h:
                    break
                cnt2, c2 = heapq.heappop(h)
                ans += c2
                cnt2 += 1
                if cnt2:
                    heapq.heappush(h, (cnt2, c2))
                heapq.heappush(h, (cnt, c))
            else:
                ans += c
                cnt += 1
                if cnt:
                    heapq.heappush(h, (cnt, c))
        return ans