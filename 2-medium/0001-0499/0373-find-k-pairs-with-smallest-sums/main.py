from typing import List
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        ans = []
        if not nums1 or not nums2:
            return ans
        
        m, n = len(nums1), len(nums2)
        h = []
        visited = set()
        heapq.heappush(h, (nums1[0] + nums2[0], 0, 0))
        visited.add((0, 0))

        while h and len(ans) < k:
            s, i, j = heapq.heappop(h)
            ans.append([nums1[i], nums2[j]])

            if j + 1 < n and (i, j + 1) not in visited:
                visited.add((i, j + 1))
                heapq.heappush(h, (nums1[i] + nums2[j + 1], i, j + 1))
            
            if i + 1 < m and (i + 1, j) not in visited:
                visited.add((i + 1, j))
                heapq.heappush(h, (nums1[i + 1] + nums2[j], i + 1, j))
        
        return ans
