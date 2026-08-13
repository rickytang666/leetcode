from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# bfs

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        maxSum, ans, level = float('-inf'), 0, 0
        q = deque()
        q.append(root)

        while q:
            n = len(q)
            level += 1
            sum = 0
            for _ in range(n):
                node = q.popleft()
                sum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if sum > maxSum:
                maxSum = sum
                ans = level
            
        return ans