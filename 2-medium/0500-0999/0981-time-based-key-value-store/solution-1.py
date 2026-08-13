class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = {'times':[], 'values':[]}
        self.store[key]['times'].append(timestamp)
        self.store[key]['values'].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ''
        times = self.store[key]['times']
        values = self.store[key]['values']

        ans = -1
        lo, hi = 0, len(times) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if times[mid] <= timestamp:
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return '' if ans == -1 else values[ans]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)