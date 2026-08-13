from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        nodes = []
        curr = head
        length = 0

        while curr:
            nodes.append(curr)
            curr = curr.next
            length += 1
        
        left, right = 0, length - 1
        tail = head

        while left < right:
            nodes[left].next = nodes[right]
            left += 1

            if left >= right:
                tail = nodes[right]

            nodes[right].next = nodes[left]
            right -= 1

            tail = nodes[left]

        # clear the end
        if tail: tail.next = None