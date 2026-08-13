from typing import Optional, List

# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        self.ans = []
        def rec(node):
            if not node: return
            for c in node.children: rec(c)
            self.ans.append(node.val)
        rec(root)
        return self.ans