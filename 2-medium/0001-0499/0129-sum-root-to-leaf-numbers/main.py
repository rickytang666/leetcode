from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def rec(node, sum):
            if not node:
                return
            sum = sum * 10 + node.val
            if not node.left and not node.right:
                self.ans += sum
                return
            rec(node.left, sum)
            rec(node.right, sum)
        rec(root, 0)
        return self.ans