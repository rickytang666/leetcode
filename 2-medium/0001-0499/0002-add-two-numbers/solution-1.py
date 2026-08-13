from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1, n2 = l1, l2
        carry = 0
        ans = ListNode(0)
        curr = ans
        while n1 or n2 or carry:
            v1 = n1.val if n1 else 0
            v2 = n2.val if n2 else 0
            sum = v1 + v2 + carry
            
            carry = sum // 10
            curr.next = ListNode(sum % 10)
            curr = curr.next

            if n1: n1 = n1.next
            if n2: n2 = n2.next
        return ans.next # remove dummy head