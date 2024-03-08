# https://leetcode.com/problems/sort-an-array/
from typing import List

class Solution:

    def merge(self, nums, left, mid, right):
        l_arr = nums[left: mid + 1]
        r_arr = nums[mid + 1: right + 1]

        l_ptr = r_ptr = 0
        nums_ptr = left    # Most important Step


        while l_ptr < len(l_arr) and r_ptr < len(r_arr):
            if l_arr[l_ptr] <= r_arr[r_ptr]:
                nums[nums_ptr] = l_arr[l_ptr]
                l_ptr += 1
            else:
                nums[nums_ptr] = r_arr[r_ptr]
                r_ptr += 1
            nums_ptr += 1
        
        while l_ptr < len(l_arr):
            nums[nums_ptr] = l_arr[l_ptr]
            l_ptr += 1; nums_ptr += 1
        
        while r_ptr < len(r_arr):
            nums[nums_ptr] = r_arr[r_ptr]
            r_ptr += 1; nums_ptr +=1 

    def mergeSort(self, nums, left, right):
        if left == right:
            return nums
        
        mid = (left + right) // 2
        self.mergeSort(nums, left, mid)
        self.mergeSort(nums, mid + 1, right)
        self.merge(nums, left, mid, right)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums, 0, len(nums) - 1)        
        return nums