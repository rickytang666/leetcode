from typing import List

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        target = total // k
        arr = [0] * k
        def dfs(i):
            if i == len(nums):
                return True
            for j in range(k):
                if j > 0 and arr[j] == arr[j - 1]:
                    continue
                if arr[j] + nums[i] <= target:
                    arr[j] += nums[i]
                    if dfs(i + 1):
                        return True
                    arr[j] -= nums[i]
            return False
        return dfs(0)
