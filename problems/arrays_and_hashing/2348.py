# https://leetcode.com/problems/number-of-zero-filled-subarrays/description/
from typing import List

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        
        # You need to pad the array with a -1 at the start and the end to make this work
        n = len(nums)

        nums.append(-1) 
        
        i, zeros_encountered_count = 0, 0
        total_subarrays = 0
        prev = -1

        # Iterate once over the entire array
        while i <= n:
            curr = nums[i]

            # If the current item is zero, just increment the counter of the encountered bit
            if curr == 0:
                zeros_encountered_count += 1
            else:
                # If I have hit a block where current item is non-zero, but all prevoius items were zero, add all the possible combinations of the zeros that could be formed using this contigous sub-array
                if prev == 0:
                    total_subarrays += (zeros_encountered_count + 1) * zeros_encountered_count // 2
                    # Reset the zeros encountered counter here
                    zeros_encountered_count = 0
            
            # Move ahead
            i += 1
            prev = curr           
        
        return total_subarrays
            

