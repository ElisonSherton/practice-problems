# https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/
from typing import List

# Linear time solution
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        result = 0

        R = len(nums) - 1

        for L in range(len(nums)):
            while (nums[L] + nums[R] > target) and L <= R:
                R -= 1
            if L <= R:
                result += 2 ** (R - L)

        return result % (10 ** 9 + 7) 

# Slightly better than following still quadratic time solution
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        
        L, n = 0, len(nums)

        num_subseq = 0
        
        # For the current leftmost position, find right we can go without going over the sum condition and then add the count of all the sets that can be made by those to our total 
        while L < n:
            this_sequence_combinations = 0
            R = L + 1
            
            # Find out if the current number can be included, do that by checking if twice of the number is lower than the target
            curr_num = nums[L]
            if curr_num * 2 <= target:
                this_sequence_combinations += 1
            
            # Move the right pointer ahead
            while R < n and curr_num + nums[R] <= target:
                R = R + 1
            
            # If there are more than zero elements which satisfy the sum condition, add those elements to our total, subtract 1 to remove the empty set from out count
            if R - L > 1:
                this_sequence_combinations += 2 ** (R - L - 1) - 1
                
            num_subseq += this_sequence_combinations
            L += 1

        return num_subseq % (10 ** 9 + 7)

# Correct thought process
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        
        nums.sort(reverse = True)
        
        L, n = 0, len(nums)

        num_subseq = 0
        
        while L < n:
            this_sequence_combinations = 0
            R = L + 1
            
            curr_num = nums[L]
            if curr_num * 2 <= target:
                this_sequence_combinations += 1
            
            while R < n and curr_num + nums[R] > target:
                R = R + 1
            
            delta = 0
            if R < n:
                this_sequence_combinations += 2 ** (n - L - 1) - 1
                if R - L > 1:
                    delta = 2 ** (R - L - 1) - 1
                    this_sequence_combinations -= delta
            
            num_subseq += this_sequence_combinations
            L += 1

        return num_subseq % (10 ** 9 + 7)