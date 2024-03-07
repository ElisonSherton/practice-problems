# https://leetcode.com/problems/product-of-array-except-self/description/

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output_array = [1]

        # Keep a running product of all the lhs elements in output array
        for element in nums[:-1]:
            last = output_array[-1]
            output_array.append(last * element)
        
        # Multiply that with running product of all the rhs elements in the output array
        prod = 1
        for i in range(len(nums) - 2, -1, -1):
            prod *= nums[i + 1]
            output_array[i] *= prod
        
        return output_array
