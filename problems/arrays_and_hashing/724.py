# https://leetcode.com/problems/find-pivot-index/description/

from typing import List

# Smarter Solution
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # Keep a track of sum of all elements on the left
        lsum = 0

        # Find out the total sum
        total = sum(nums)

        # Move L-R
        for idx, element in enumerate(nums):
            
            # RHS Sum will be equal to the total - LHS Sum - current element value
            rsum = total - element - lsum
            
            if rsum == lsum:
                return idx
            
            lsum += element
        
        # If still not returned, we have iterated through the whole list, hence return -1
        return -1

# Trivial Solution
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        # Have an array store the sum of all the elements to the left 
        cum_sum_left = [0]
        for i in nums[:-1]:
            cum_sum_left.append(cum_sum_left[-1] + i)

        # Have an array store the sum of all the elements to the right        
        cum_sum_right = [0]
        for i in nums[::-1][:-1]:
            cum_sum_right.append(cum_sum_right[-1] + i)
        
        # Check an array where lsum = rsum
        for i in range(len(nums)):
            if cum_sum_left[i] == cum_sum_right[len(nums) - i - 1]:
                return i
        
        return -1
        