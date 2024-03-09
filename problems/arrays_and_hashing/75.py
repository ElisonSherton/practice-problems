# https://leetcode.com/problems/sort-colors/description/
from typing import List

# Best Solution: Single pass through the list and sort in place
class Solution:

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left_ptr = 0
        right_ptr = len(nums) - 1
        curr_ptr = -1

        while curr_ptr < right_ptr:

            curr_ptr += 1

            if nums[curr_ptr] == 0:
                nums[curr_ptr], nums[left_ptr] = nums[left_ptr], nums[curr_ptr]
                left_ptr += 1
            
            if nums[curr_ptr] == 2:
                nums[curr_ptr], nums[right_ptr] = nums[right_ptr], nums[curr_ptr]
                right_ptr -= 1
                curr_ptr -= 1        

# Better solution 
# O(n) TC (But 2 passes through the list) and O(1) Space Complexity
class Solution:

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Keep a track of number of 0s, 1s, 2s
        nums_counter = {0: 0, 1: 0, 2: 0}

        for element in nums:
            nums_counter[element] += 1
        
        # Overwrite the nums array based on counts obtained above
        nums_idx = 0
        for k in [0, 1, 2]:
            reps = nums_counter[k]
            for _ in range(reps):
                nums[nums_idx] = k
                nums_idx += 1
        

# Trivial Solution -> MergeSort
class Solution:

    def merge(self, arr, left, right):
        mid = (left + right) // 2
        larr = arr[left: mid + 1]
        rarr = arr[mid + 1: right + 1]

        curr_ptr, lptr, rptr = left, 0, 0

        while (lptr < len(larr)) and (rptr < len(rarr)):
            if larr[lptr] < rarr[rptr]:
                arr[curr_ptr] = larr[lptr]
                lptr += 1
            elif larr[lptr] >= rarr[rptr]:
                arr[curr_ptr] = rarr[rptr] 
                rptr += 1
            curr_ptr += 1

        while lptr < len(larr):
            arr[curr_ptr] = larr[lptr]
            curr_ptr += 1
            lptr += 1

        while rptr < len(rarr):
            arr[curr_ptr] = rarr[rptr]
            curr_ptr += 1
            rptr += 1

    def mergeSort(self, arr, left, right):
        if left == right:
            return arr
        
        mid = (left + right) // 2
        self.mergeSort(arr, left, mid)
        self.mergeSort(arr, mid + 1, right)
        self.merge(arr, left, right)


    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.mergeSort(nums, 0, len(nums) - 1)