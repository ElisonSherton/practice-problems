# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

from typing import List

# Much better elegant solution
class Solution:
        
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        L, R = 0, len(numbers) - 1

        while L < R:
            l_elem, r_elem = numbers[L], numbers[R]

            s = l_elem + r_elem

            if s > target:
                R = R - 1
            elif s < target:
                L = L + 1
            else:
                return [L + 1, R + 1]
        
        return [-1, -1]

# Working solution
class Solution:

    def binSearch(self, numbers: List[int], to_find: int) -> int:
        low, high = 0, len(numbers)

        if to_find > numbers[-1] or to_find < numbers[0]:
            return -1

        while low + 1 < high:
            mid = (low + high) // 2
            if numbers[mid] > to_find:
                high = mid
            elif numbers[mid] < to_find:
                low = mid
            else:
                return mid
        
        return -1
        
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for idx, element in enumerate(numbers):
            to_find = target - element
            find_idx = self.binSearch(numbers, to_find)

            if (find_idx != -1) and (idx != find_idx):
                l, r = min(idx, find_idx), max(idx, find_idx)
                return [l + 1, r + 1]
        
        return [-1, -1]