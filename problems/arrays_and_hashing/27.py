# https://leetcode.com/problems/remove-element/description/

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        p1 = 0
        p2 = len(nums) - 1

        # Check if it's a single element list
        if p1 == p2:
            if nums[p1] == val: 
                return 0 
            return 1

        # While left pointer does not cross the right pointer
        while p1 < p2:
            # If current element is not the one to be removed, keep moving forward
            if nums[p1] != val:
                p1 += 1
            else:
                while True:
                    # If current element is the one to be removed check if the right pointer is containing same element as the val, if so, keep moving the right pointer towards left
                    if nums[p2] == val:
                        p2 -= 1
                        if p2 <= 0: return 0
                        if p2 <= p1: return p1
                    else:
                        # If element from right is not the same as val, then swap the elments pointed to by p1 and p2
                        nums[p1], nums[p2] = nums[p2], nums[p1]
                        p1 += 1; p2 -= 1
                        break

        # If the list only had one single element multiple times, we would not have checked the entire list and hence one final check is needed here
        if p1 == p2:
            if nums[p1] != val:
                p1 += 1
        return p1