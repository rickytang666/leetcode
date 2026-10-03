from bisect import bisect_left, bisect_right

class MyCalendar:

    def __init__(self):
        self.bounds = []

    def book(self, startTime: int, endTime: int) -> bool:
        i = bisect_right(self.bounds, startTime)
        if i % 2 or bisect_left(self.bounds, endTime) != i:
            return False
        self.bounds[i:i] = (startTime, endTime)
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)
