from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.indices = {val : i for i, val in enumerate(inorder)}
        self.pos = 0
        def rec(left, right):
            if left > right: return None
            val = preorder[self.pos]
            self.pos += 1
            root = TreeNode(val)

            mid = self.indices[val]

            root.left = rec(left, mid - 1)
            root.right = rec(mid + 1, right)

            return root
        return rec(0, len(inorder) - 1)