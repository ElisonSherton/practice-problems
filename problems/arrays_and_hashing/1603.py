# https://leetcode.com/problems/design-parking-system/description/

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.total = {1: big, 2: medium, 3: small}
        self.occupied = {1: 0, 2: 0, 3: 0}
        

    def addCar(self, carType: int) -> bool:

        if self.occupied[carType] < self.total[carType]:
            self.occupied[carType] += 1
            return True
        
        return False

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)