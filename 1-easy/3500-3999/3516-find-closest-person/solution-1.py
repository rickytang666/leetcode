class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        dx, dy = abs(x - z), abs(y - z)
        if dx < dy:
            return 1
        elif dy < dx: 
            return 2
        else:
            return 0