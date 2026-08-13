
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        while curr:
            v = curr.val
            if p.val < v and q.val < v:
                curr = curr.left
            elif p.val > v and q.val > v:
                curr = curr.right
            else:
                return curr
        return curr