# https://leetcode.com/problems/container-with-most-water/

from typing import List

# Linear run time solution
class Solution:
    def maxArea(self, height: List[int]) -> int:
        current_max = -float("inf")

        if len(height) == 1:
            return 0

        L, R = 0, len(height) - 1

        while L < R:
            area = (R - L) * min(height[L], height[R])
            if area > current_max:
                current_max = area
            
            if height[L] > height[R]:
                R = R - 1
            else:
                L = L + 1
        
        return max(current_max, 0)


# First Solution
class Solution:
    def maxArea(self, height: List[int]) -> int:
        current_max = -float("inf")

        max_areas = []

        for L in range(n):
            curr = height[L]

            # Only if the next height is bigger than all of the heights observed so far from the left, then do a computation of max area. 
            if curr > current_max:
                current_max = curr
                max_area = -float("inf")
                
                for j in range(n - 1, L, -1):
                    a = min(curr, height[j]) * (j - L)
                    if a > max_area:
                        max_area = a

                max_areas.append(max_area)
        
        return max(max_areas)