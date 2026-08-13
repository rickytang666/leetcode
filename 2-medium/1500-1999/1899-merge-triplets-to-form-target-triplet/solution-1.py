from typing import List

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x = y = z = False
        for a, b, c in triplets:
            x |= (a == target[0] and b <= target[1] and c <= target[2])
            y |= (b == target[1] and a <= target[0] and c <= target[2])
            z |= (c == target[2] and a <= target[0] and b <= target[1])
            if x and y and z:
                return True
        return False