from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tail, node = head, head.next
        while node:
            if node.val:
                tail.val += node.val
            elif node.next:
                tail.next = node
                tail = node
            else:
                tail.next = None
            node = node.next
        return head