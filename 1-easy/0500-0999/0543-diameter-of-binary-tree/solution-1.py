from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.d = 0

        def rec(node):
            if not node: return 0
            ld, rd = rec(node.left), rec(node.right)
            self.d = max(self.d, ld + rd)
            return max(ld, rd) + 1
        
        rec(root)
        return self.d