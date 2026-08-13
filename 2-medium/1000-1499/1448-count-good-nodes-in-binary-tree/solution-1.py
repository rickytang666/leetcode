
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def rec(node, maxSoFar):
            if not node: return 0
            good = 1 if node.val >= maxSoFar else 0
            maxSoFar = max(maxSoFar, node.val)
            return good + rec(node.left, maxSoFar) + rec(node.right, maxSoFar)
        return rec(root, float('-inf'))