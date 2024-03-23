# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/
from typing import List



# Working solution
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        L = R = k = 0
        stop = len(nums)

        while True:
            if R >= stop:
                break

            # Advance the right pointer till we hit a different element than left pointer
            while R < stop and nums[L] == nums[R]:
                R = R + 1
            
            # Find out how many steps should the left pointer advance
            ahead_steps = R - L
            # If it is within 2 steps, then no issues
            if ahead_steps <= 2:
                L = L + ahead_steps
                R = L
                k = k + ahead_steps
            # Otherwise, we need to pull back the rest of the array ahead of R to index L + 2
            else:
                pull_back = ahead_steps - 2
                for L_step, i in enumerate(range(R, stop)):
                    nums[L + 2 + L_step], nums[i] = nums[i], nums[L + 2 + L_step]
                stop = stop - pull_back
                L += 2; R = L; k += 2
        
        return k

            

                    