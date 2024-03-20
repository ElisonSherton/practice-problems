# https://leetcode.com/problems/sign-of-the-product-of-an-array/

from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        counts = {1: 0, 0: 0, -1: 0}
        for element in nums:
            if element > 0:
                counts[1] += 1
            elif element < 0:
                counts[-1] += 1
            else:
                return 0
        
        if counts[-1] % 2 == 1:
            return -1
        
        return 1