from typing import List

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen, l, cur, best = set(), 0, 0, 0
        for x in nums:
            while x in seen:
                seen.remove(nums[l])
                cur -= nums[l]
                l += 1
            seen.add(x)
            cur += x
            best = max(best, cur)
        return best