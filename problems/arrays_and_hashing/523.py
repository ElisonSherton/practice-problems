# https://leetcode.com/problems/continuous-subarray-sum/
from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        n = len(nums)

        for i in range(n):
            nums[i] %= k

        # Initialize so that you asume there's a zero as the prefix of current position
        remainder_map = {0: -1}
        cum_sum = 0
        
        for idx, element in enumerate(nums, start = 0):
            cum_sum += element
            remainder = cum_sum % k

            if remainder not in remainder_map:
                remainder_map[remainder] = idx
            # If you reached an index where the remainder is repeated that means we have accumulated a multiple of k
            elif idx - remainder_map[remainder] > 1:
                return True
        
        return False

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        n = len(nums)

        for i in range(n):
            nums[i] %= k

        remainder_map = {0: [-1]}
        cum_sum = 0
        
        for idx, element in enumerate(nums[:], start = 0):
            cum_sum += element
            remainder = cum_sum % k

            index_list = remainder_map.get(remainder, [])
            index_list.append(idx)

            remainder_map[remainder] = index_list
        
        
        for k, v in remainder_map.items():
            if len(v) > 1:
                if v[-1] - v[0] >= 2:
                    return True
        return False


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        n = len(nums)

        for i in range(n):
            nums[i] %= k

        cumulative_array = [nums[0]]
        for element in nums[1:]:
            cumulative_array.append(element + cumulative_array[-1])
        
        for i in range(n):
            decrement = 0 if i == 0 else cumulative_array[i - 1]

            for j in range(i + 1, n):
                curr_sum = cumulative_array[j] - decrement
                # print(i, j, curr_sum)
                if (curr_sum % k == 0): #and ((j - i) >= 2)
                    return True
        
        return False