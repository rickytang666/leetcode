from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.result = 0
        self.cache = {0 : 1}
        self.dfs(root, targetSum, 0)
        return self.result
    
    def dfs(self, root, target, currSum):
        if not root:
            return
        currSum += root.val
        oldSum = currSum - target

        self.result += self.cache.get(oldSum, 0)
        self.cache[currSum] = self.cache.get(currSum, 0) + 1

        self.dfs(root.left, target, currSum)
        self.dfs(root.right, target, currSum)

        self.cache[currSum] -= 1