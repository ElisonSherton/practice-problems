# https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/description/
from typing import List

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        
        nums = sorted(nums)
        if len(nums) == 1: return 0

        min_diff = float("inf")

        L = 0; R = 0
        

        while R < len(nums):
            if R - L + 1  == k:
                delta = nums[R] - nums[L]
                min_diff = min(delta, min_diff)
                L += 1
            R += 1
        
        return min_diff              