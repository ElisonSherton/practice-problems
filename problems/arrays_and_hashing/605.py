# https://leetcode.com/problems/can-place-flowers/description/
from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        can_plant_count = 0
        left = -1; right = 1
        total_space = len(flowerbed)

        # Check the edge case of just one single flowerbed
        if total_space == 1 and flowerbed[0] == 0:
            return 1 >= n

        for i in range(total_space):
            c = flowerbed[i]
            
            # If currently, we have a plant, we cannot replant
            if c == 1: 
                left += 1; right += 1
                continue
            # If we have both neighbours, need to check them 
            elif (left > -1) and (right < total_space):
                # If neighbours don't have any plant, I can plant in current position
                if flowerbed[left] != 1 and flowerbed[right] != 1: 
                    flowerbed[i] = 1
                    can_plant_count += 1
            elif left == -1:
                # My only neighbour is right, so just check the right neighbour
                if flowerbed[right] != 1: 
                    flowerbed[i] = 1
                    can_plant_count += 1
            elif right == total_space:
                # My only neighbour is left, so just check the right neighbour
                if flowerbed[left] != 1:
                    flowerbed[i] = 1
                    can_plant_count += 1

            left += 1
            right += 1

        return can_plant_count >= n
