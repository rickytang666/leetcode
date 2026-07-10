from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        queue = deque([root])
        lr = True

        while queue:
            levelSize = len(queue)
            levelVals = deque()

            for _ in range(levelSize):
                node = queue.popleft()

                if lr:
                    levelVals.append(node.val)
                else:
                    levelVals.appendleft(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            ans.append(list(levelVals))
            lr = not lr
        
        return ans