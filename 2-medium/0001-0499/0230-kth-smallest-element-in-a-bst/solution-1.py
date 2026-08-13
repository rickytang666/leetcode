from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # naive solution
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        def rec(node):
            if not node: return
            arr.append(node.val)
            rec(node.left)
            rec(node.right)
        rec(root)
        return sorted(arr)[k - 1]