class UndergroundSystem:

    def __init__(self):
        self.active = {}
        self.trips = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.active[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start, t0 = self.active.pop(id)
        if (start, stationName) not in self.trips:
            self.trips[(start, stationName)] = [0, 0]
        self.trips[(start, stationName)][0] += t - t0
        self.trips[(start, stationName)][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, count = self.trips[(startStation, endStation)]
        return total / count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
