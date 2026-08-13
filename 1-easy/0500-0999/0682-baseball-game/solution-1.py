from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        arr = []
        for o in operations:
            if o == '+':
                arr.append(arr[-2] + arr[-1])
            elif o == 'D':
                arr.append(2 * arr[-1])
            elif o == 'C':
                arr.pop()
            else:
                arr.append(int(o))
        return sum(arr)