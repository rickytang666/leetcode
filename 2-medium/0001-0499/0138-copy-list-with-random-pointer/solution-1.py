from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None

        # interweave
        curr = head
        while curr:
            newNode = Node(curr.val, curr.next)
            curr.next = newNode
            curr = newNode.next
        
        # set random
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        # separate the lists
        oldHead = head
        newHead = head.next
        currOld = oldHead
        currNew = newHead

        while currOld:
            currOld.next = currOld.next.next
            currNew.next = currNew.next.next if currNew.next else None
            currOld = currOld.next
            currNew = currNew.next
        
        return newHead
