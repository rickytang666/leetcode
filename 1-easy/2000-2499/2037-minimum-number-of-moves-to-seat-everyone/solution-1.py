from typing import List

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        return sum(abs(pos1 - pos2) for pos1, pos2 in zip(sorted(students), sorted(seats)))