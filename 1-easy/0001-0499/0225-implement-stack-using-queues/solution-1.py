class MyStack:

    def __init__(self):
        self.s = []

    def push(self, x: int) -> None:
        self.s.append(x)

    def pop(self) -> int:
        return self.s.pop()

    def top(self) -> int:
        return self.s[-1]

    def empty(self) -> bool:
        return False if self.s else True
    