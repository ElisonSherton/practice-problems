# https://leetcode.com/problems/move-zeroes/

from typing import List

# Working solution
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Make a list of all the zero indices
        zero_idxs = []

        for idx, element in enumerate(nums):
            if element == 0:
                zero_idxs.append(idx)
        
        zero_idxs.append(len(nums))
        
        # Between first element and first zero index, no swapping, from first to second zero index, swap once, from second to third zero index swap thrice etc. This will lead to pushing of all the zeros right to the end of the array.
        for num_repeats, (start, end) in enumerate(zip(zero_idxs[:-1], zero_idxs[1:]), start = 1):
            for i in range(start + 1, end):
                nums[i], nums[i - num_repeats] = nums[i - num_repeats], nums[i]