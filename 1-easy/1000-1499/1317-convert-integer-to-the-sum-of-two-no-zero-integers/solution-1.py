from typing import List
import math

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def isNoZero(num):
            while num:
                rem = num % 10
                if rem == 0: return False
                num //= 10
            return True
        for a in range(1, math.ceil(n / 2)):
            b = n - a
            if isNoZero(a) and isNoZero(b):
                return [a, b]
        return [1, n - 1]