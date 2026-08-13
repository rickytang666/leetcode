from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# O(n) time complexity, O(1) space complexity
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse 2nd half
        prev, curr = None, slow
        while curr:
            temp = curr.next
            curr.next = prev
            
            prev = curr
            curr = temp
        
        ans = 0
        left, right = head, prev
        while right:
            ans = max(ans, left.val + right.val)
            left = left.next
            right = right.next
        
        return ans