from typing import List

class Bank:

    def __init__(self, balance: List[int]):
        self.arr = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        n = len(self.arr)
        if 1 <= account1 <= n and 1 <= account2 <= n:
            if self.arr[account1 - 1] >= money:
                self.arr[account1 - 1] -= money
                self.arr[account2 - 1] += money
                return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        n = len(self.arr)
        if 1 <= account <= n:
            self.arr[account - 1] += money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        n = len(self.arr)
        if 1 <= account <= n and self.arr[account - 1] >= money:
            self.arr[account - 1] -= money
            return True
        return False

# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
