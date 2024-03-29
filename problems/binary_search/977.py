# https://leetcode.com/problems/squares-of-a-sorted-array/

from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Find where the sign changes O(n)
        sign_change_idx = -1
        for L in range(0, n - 1):
            if nums[L+1] > 0 and nums[L] <= 0:
                sign_change_idx = L
        
        new_nums = []
        # If the sign changes, then do this (O(n))
        if sign_change_idx != -1:

            # Use two pointer technique
            start = sign_change_idx
            L, R = start, start + 1

            while L > -1 and R < n:
                # Move left and right respectively selecting the numbers in ascending order of the absolute value in nums
                if abs(nums[L]) >= abs(nums[R]):
                    new_nums.append(abs(nums[R]))
                    R = R + 1
                else:
                    new_nums.append(abs(nums[L]))
                    L = L - 1
            # Add the remainder of the values to the new nums
            if L >= 0:
                for x in range(L, -1, -1):
                    new_nums.append(abs(nums[x]))
            elif R < n:
                for x in range(R, n, 1):
                    new_nums.append(abs(nums[x]))     
        # If it doesn't change and it's on the other side of number line reverse the list    
        elif nums[0] < 0:
            new_nums = nums[::-1]
        # Otherwise use the same list
        else:
            new_nums = nums

        # O(n) => O(3n) = O(n)
        return [x ** 2 for x in new_nums]
