#Did this problem by myself. Minor corrections so checked solution, but did 99% of it my own


from collections import defaultdict
class UndergroundSystem:

    def __init__(self, intime = defaultdict(), stationpairs = defaultdict(list)):
        # intime = self.intime
        # stationpairs = self.stationpairs
        # intime = defaultdict(set)
        # stationpairs = defaultdict(list) #stationpair[(stationnames)] = list of all the timeins
        self.intime = intime
        self.stationpairs = stationpairs
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.intime[id] = [stationName,t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        #timein  = 0
        if id in self.intime:
            instation,in_time = self.intime.pop(id)
            timein = t - in_time
            self.stationpairs[(instation, stationName)].append(timein)
            # self.stationpairs[(instation, stationName)][1] +=1
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        if (startStation, endStation) in self.stationpairs:
            alltimes = self.stationpairs[(startStation, endStation)]
            res = sum(alltimes)/len(alltimes)
            return res
            


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
