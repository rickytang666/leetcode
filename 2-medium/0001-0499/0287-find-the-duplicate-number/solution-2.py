from typing import List

# Floyd’s Tortoise and Hare (treat as a linked list)
# it can be easily proved that there'll ALWAYS be a loop when there's a duplicate

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[0]
        # finding cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: break
        # finding entrance to cycle
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow