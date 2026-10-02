from typing import List

class ATM:

    NOTES = (20, 50, 100, 200, 500)

    def __init__(self):
        self.storage = [0] * 5

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5):
            self.storage[i] += banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        ans = [0] * 5
        for i in reversed(range(5)):
            ans[i] = min(self.storage[i], amount // self.NOTES[i])
            amount -= ans[i] * self.NOTES[i]
        if amount > 0:
            return [-1]
        for i in range(5):
            self.storage[i] -= ans[i]
        return ans


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)
