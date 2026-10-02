from bisect import bisect_right
from operator import itemgetter

class SnapshotArray:

    def __init__(self, length: int):
        self.id = 0
        self.history = [[(0, 0)] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        self.history[index].append((self.id, val))

    def snap(self) -> int:
        self.id += 1
        return self.id - 1

    def get(self, index: int, snap_id: int) -> int:
        h = self.history[index]
        return h[bisect_right(h, snap_id, key=itemgetter(0)) - 1][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
