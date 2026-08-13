from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = l1
        arr1 = []
        arr2 = []
        while curr:
            arr1.append(curr.val)
            curr = curr.next
        arr1.reverse()
        curr = l2
        while curr:
            arr2.append(curr.val)
            curr = curr.next
        arr2.reverse()
        final = []
        i = j = carry = 0
        while i < len(arr1) or j < len(arr2) or carry:
            x = arr1[i] if i < len(arr1) else 0
            y = arr2[j] if j < len(arr2) else 0
            sum = x + y + carry
            final.append(sum % 10)
            carry = sum // 10
            i += 1
            j += 1
        head = ListNode(0, None)
        curr = head
        for a in range(len(final) - 1, -1, -1):
            curr.next = ListNode(final[a], None)
            curr = curr.next
        return head.next