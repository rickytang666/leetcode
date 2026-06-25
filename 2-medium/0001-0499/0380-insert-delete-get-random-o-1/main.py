import random

class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.mp = {} # val -> index

    def insert(self, val: int) -> bool:
        if val in self.mp: return False
        self.arr.append(val)
        self.mp[val] = len(self.arr) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.mp: return False
        i = self.mp[val]
        self.arr[i] = self.arr[-1]
        self.mp[self.arr[-1]] = i
        self.arr.pop()
        del self.mp[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)