# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

from typing import List

# Much Smart Solution
# Refer this for more details: https://www.youtube.com/watch?v=8i-f24YFWC4
# Basically we use the given array to keep track of which elements appeared in the array by using indices of the array as they too run from 0 to n-1
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        for element in nums:
            set_val = abs(element) - 1
            curr_elem = nums[set_val]
            nums[set_val] = -abs(curr_elem)

        return [idx + 1 for idx, element in enumerate(nums) if element > 0] 

# Trivial Solution
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        range1n = set(range(1, len(nums) + 1))

        for element in nums:
            if element in range1n:
                range1n.remove(element)
        
        return list(range1n)