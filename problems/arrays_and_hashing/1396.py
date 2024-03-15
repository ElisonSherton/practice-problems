# https://leetcode.com/problems/design-underground-system/description/
from typing import List

# Working solution
class UndergroundSystem:

    def __init__(self):
        self.travellers = {}
        self.stations = {}
        
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.travellers[id]= {"start": t, "station": stationName}
        
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_time, start_station = self.travellers[id]["start"], self.travellers[id]["station"]
        self.travellers[id] = {}

        # Find the current time taken
        duration = t - start_time
        end_station = stationName

        if start_station in self.stations:
            # If the start and end stations have been encountered once, simply append the duration to the existing list
            if end_station in self.stations[start_station]:
                self.stations[start_station][end_station].append(duration)     
            # Create a new entry for this end station in the current start station
            else:
                self.stations[start_station][end_station] = [duration]
        # Create a new entry for this start station
        else:
            self.stations[start_station] = {stationName: [duration]}
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        durations = self.stations[startStation][endStation]
        return sum(durations) / len(durations)


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)