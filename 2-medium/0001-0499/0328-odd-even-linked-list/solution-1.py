from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        if not head.next: return head
        odd_head = head
        even_head = head.next
        is_odd = 1
        odd_curr = odd_head
        even_curr = even_head
        it = even_head.next
        while it:
            if is_odd:
                odd_curr.next = it
                odd_curr = odd_curr.next
            else:
                even_curr.next = it
                even_curr = even_curr.next
            is_odd ^= 1
            it = it.next
        even_curr.next = None
        odd_curr.next = even_head
        return odd_head