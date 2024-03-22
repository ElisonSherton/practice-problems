# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        unique_list = [nums[0]]

        for L in range(1, len(nums)):
            if nums[L] == unique_list[-1]:
                continue
            else:
                unique_list.append(nums[L])

        for idx, i in enumerate(unique_list):
            nums[idx] = i 
        
        return len(unique_list)