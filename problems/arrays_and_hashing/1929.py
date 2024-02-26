# https://leetcode.com/problems/concatenation-of-array/description/
from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        total_length = len(nums)
        final_nums = []
        for i in range(2 * total_length):
            element = i % total_length
            final_nums.append(nums[element])
        return final_nums