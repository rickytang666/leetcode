from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# O(n) time complexity, O(n) space complexity
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        ans = -1
        n = len(arr)
        for i in range(n // 2):
            ans = max(ans, arr[i] + arr[n - 1 - i])
        return ans