# https://leetcode.com/problems/range-sum-query-immutable/

from typing import List

# Optimal Solution
# Maintain a cumulative sum list and use it to answer queries by subtracting the cumsum to the left of the left index of the given range
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.cum_sum = [self.nums[0]]
        for element in self.nums[1:]:
            self.cum_sum.append(self.cum_sum[-1] + element)
        print(self.cum_sum)
        
    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.cum_sum[right]
        else:
            return self.cum_sum[right] - self.cum_sum[left - 1]    

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
        
# Trivial Solution
class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.cum_sum = [self.nums[0]]
        for element in self.nums[1:]:
            self.cum_sum.append(self.cum_sum[-1] + element)
        print(self.cum_sum)
        
    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:(right + 1)])
    
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)        