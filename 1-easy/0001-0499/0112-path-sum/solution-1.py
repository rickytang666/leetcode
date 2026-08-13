from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, curr):
            if not node:
                return False
            curr += node.val
            if not node.left and not node.right:
                return curr == targetSum
            return dfs(node.left, curr) or dfs(node.right, curr)
        return dfs(root, 0)