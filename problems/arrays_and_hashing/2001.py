# https://leetcode.com/problems/number-of-pairs-of-interchangeable-rectangles/
from typing import List


class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        
        # Create a hashmap of all rectangles having same aspect ratio
        # Key - AR, Value - Count
        ars = {}
        for rect in rectangles:
            ar = rect[1] / rect[0]
            ars[ar] = 1 + ars.get(ar, 0)
        
        total_int = 0

        # For all those ARs where there are more than 2 rectngles, just compute the nC2 for it i.e. n * (n-1) // 2
        for k, n in ars.items():
            if n > 1:
                total_int += n * (n - 1) // 2
        
        return total_int