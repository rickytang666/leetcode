from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(node, wentLeft, steps):
            if node:
                self.ans = max(self.ans, steps)
                if wentLeft:
                    dfs(node.right, False, steps + 1)
                    dfs(node.left, True, 1)
                else:
                    dfs(node.left, True, steps + 1)
                    dfs(node.right, False, 1)
        
        dfs(root, True, 0)
        return self.ans