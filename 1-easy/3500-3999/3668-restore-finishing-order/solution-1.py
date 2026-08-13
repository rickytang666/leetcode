from typing import List

class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        ans = []
        friendSet = set(friends)
        for o in order:
            if o in friendSet: ans.append(o)
        return ans