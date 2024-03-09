# https://leetcode.com/problems/brick-wall/
from typing import List, Dict

# Efficient Solution
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        wall_width = sum(wall[0])
        wall_height = len(wall)

        num_cuts: Dict[int,int] = {}

        for row in wall:
            cum_sum = [row[0]]
            for element in row[1:]:
                cum_sum.append(element + cum_sum [-1])
            
            # Make sure the last element is always the width of the wall
            if cum_sum[-1] != wall_width:
                assert "Incorrect Row"
            
            # Save which positions are suitable for cutting for each row to avoid being cut
            for element in cum_sum:
                if element in num_cuts:
                    num_cuts[element] += 1
                else:
                    num_cuts[element] = 1
            
        num_cuts.pop(0, None)
        num_cuts.pop(wall_width, None)

        # If there is no position except start and end this means all rows have equal width
        if len(num_cuts) == 0:
            return wall_height

        # Find where we have minimum cuts by finding max of where cuts should be avoided
        return wall_height - max(list(num_cuts.values()))
            
                
            


# Working Solution
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        wall_width = sum(wall[0])
        wall_height = len(wall)

        if wall_width == 1:
            return wall_height
        
        num_cuts: Dict[int, int]= {}

        for row in wall:
            cum_sum = [row[0]]
            for element in row[1:]:
                cum_sum.append(element + cum_sum [-1])
            
            if cum_sum[-1] != wall_width:
                assert "Incorrect Row"
            
            cum_sum = set(cum_sum)
            for i in range(wall_width + 1):
                if not i in cum_sum:
                    if i in num_cuts:
                        num_cuts[i] += 1
                    else:
                        num_cuts[i] = 1
            # print(num_cuts)

        num_cuts.pop(0, None)
        num_cuts.pop(wall_width, None)

        return min(list(num_cuts.values()))
            
                
            
