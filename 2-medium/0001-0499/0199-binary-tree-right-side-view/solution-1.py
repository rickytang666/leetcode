from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def rec(node, level):
            if not node: return
            if level > len(ans) - 1:
                ans.append(node.val)
            rec(node.right, level + 1)
            rec(node.left, level + 1)
        rec(root, 0)
        return ans