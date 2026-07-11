from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.ans = float('inf')
        self.prev = -1

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            if self.prev != -1:
                self.ans = min(self.ans, node.val - self.prev)
            self.prev = node.val
            dfs(node.right)
        
        dfs(root)
        return self.ans