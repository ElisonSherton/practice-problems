# https://leetcode.com/problems/majority-element/description/
from typing import List

# Better solution O(n) time; O(1) space
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_element = None
        freq = 0

        for element in nums:
            if freq == 0:
                majority_element = element
                freq = 1
                continue

            if element == majority_element:
                freq += 1
            else:
                freq -= 1
        
        return majority_element


# Trivial Solution -> O(n) time, O(n) space
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}

        for element in nums:
            try:
                counts[element] += 1
            except KeyError as e:
                counts[element] = 1
        
        majority_element = None
        max_freq = 0
        for k in counts:
            if counts[k] > max_freq:
                max_freq = counts[k]
                majority_element = k
        
        return majority_element
