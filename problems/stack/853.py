# https://leetcode.com/problems/car-fleet/

from typing import List

# Working solution but long
class Solution:

    def meet(self, target, car_i, car_j):
        p_i, v_i = car_i
        p_j, v_j = car_j

        if v_j == v_i:
            if p_j == p_i:
                return True, p_j
            else:
                return False, -1

        meet_time = (p_i - p_j) / (v_j - v_i)
        meet_pos = p_i + meet_time * v_i


        if (meet_time >= 0) and meet_pos <= target:
            return True, meet_pos

        return False, -1

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        
        # Sort on basis of position first
        pairs = list(zip(position, speed))
        pairs = sorted(pairs, key = lambda x: x[0], reverse = True)
        position = [x[0] for x in pairs]
        speed = [x[1] for x in pairs]
        
        fleet_stack = [(position[0], speed[0])]

        for idx, (p, v) in enumerate(zip(position[1:], speed[1:])):
            merge = False
            temp_stack = []
            while not merge and fleet_stack:
                top = fleet_stack.pop()
                meet, meet_pos = self.meet(target, top, (p, v))
                if meet:
                    merge = True
                    fleet = (max(p, top[0]), min(v, top[1]))
                    temp_stack.append(fleet)  
                else:       
                    temp_stack.append(top)          
            
            if not merge:
                temp_stack.append((p, v))

            while temp_stack:
                fleet_stack.append(temp_stack.pop())
        
        return len(fleet_stack)
