from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        self.total = 0
        def dfs(node, parent, grand):
            if not node:
                return
            if grand % 2 == 0:
                self.total += node.val
            dfs(node.left, node.val, parent)
            dfs(node.right, node.val, parent)
        dfs(root, 1, 1)
        return self.total