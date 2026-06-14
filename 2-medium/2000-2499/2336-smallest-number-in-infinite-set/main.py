import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.smallest = 1
        self.s = []
        self.in_heap = set()

    def popSmallest(self) -> int:
        if self.s:
            val = heapq.heappop(self.s)
            self.in_heap.discard(val)
            return val
        else:
            self.smallest += 1
            return self.smallest - 1

    def addBack(self, num: int) -> None:
        if num < self.smallest and num not in self.in_heap:
            heapq.heappush(self.s, num)
            self.in_heap.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
# @lc code=end

