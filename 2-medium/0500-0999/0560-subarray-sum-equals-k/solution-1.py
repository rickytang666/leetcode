from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        cnt = 0
        freq = {0 : 1}

        for n in nums:
            prefix += n

            if prefix - k in freq:
                cnt += freq[prefix - k]

            freq[prefix] = freq.get(prefix, 0) + 1
        
        return cnt