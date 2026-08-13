from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        small, big = ListNode(0, None), ListNode(0, None)
        s, b = small, big
        curr = head
        
        while curr:
            if curr.val < x:
                s.next = curr
                s = curr
            else:
                b.next = curr
                b = curr
            curr = curr.next
        
        b.next = None
        s.next = big.next
        return small.next