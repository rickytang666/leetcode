class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        # euclidean algorithm
        if num1 * num2 == 0: return 0
        elif num1 >= num2:
            return num1 // num2 + self.countOperations(num2, num1 % num2)
        else:
            return self.countOperations(num2, num1)