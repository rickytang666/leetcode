class Node:
    def __init__(self, val, p, n):
        self.val, self.prev, self.next = val, p, n

class MyCircularQueue:

    def __init__(self, k: int):
        self.cap = k
        self.dstart = Node(-1, None, None)
        self.dend = Node(-1, self.dstart, None)
        self.dstart.next = self.dend

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False

        n = Node(value, self.dend.prev, self.dend)
        self.dend.prev.next = n
        self.dend.prev = n
        self.cap -= 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        self.dstart.next = self.dstart.next.next
        self.dstart.next.prev = self.dstart
        self.cap += 1
        return True

    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.dstart.next.val

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.dend.prev.val

    def isEmpty(self) -> bool:
        return self.dstart.next == self.dend

    def isFull(self) -> bool:
        return self.cap == 0


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()