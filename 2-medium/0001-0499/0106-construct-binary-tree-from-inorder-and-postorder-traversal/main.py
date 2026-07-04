from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        self.indices = {val : i for i, val in enumerate(inorder)}
        self.pos = len(postorder) - 1
        def rec(l, r):
            if l > r:
                return None
            root_val = postorder[self.pos]
            root = TreeNode(root_val)
            idx = self.indices[root_val]
            self.pos -= 1
            root.right = rec(idx + 1, r)
            root.left = rec(l, idx - 1)
            return root
        return rec(0, len(inorder) - 1)    
