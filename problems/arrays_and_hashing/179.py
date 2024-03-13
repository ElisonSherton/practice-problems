# https://leetcode.com/problems/largest-number/description/

from functools import cmp_to_key
from typing import List

class Solution:

    def compare(self, n1, n2):
        e1 = int(str(n1) + str(n2))
        e2 = int(str(n2) + str(n1))
        if e1 > e2:
            return -1
        return 1
        
    def largestNumber(self, nums: List[int]) -> str:
        nums = sorted(nums, key=cmp_to_key(self.compare))
        out =  "".join([str(x) for x in nums])
        if int(out) == 0:
            out = "0"
        return out