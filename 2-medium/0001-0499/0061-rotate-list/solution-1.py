from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return None
        
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next
        
        k %= n
        if n == 1 or k == 0: return head

        i = 1
        curr = head

        while i < n - k:
            curr = curr.next
            i += 1
        
        nxt = curr.next
        curr.next = None
        curr = nxt

        while curr.next:
            curr = curr.next

        curr.next = head
        return nxt