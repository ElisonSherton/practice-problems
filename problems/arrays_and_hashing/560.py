# https://leetcode.com/problems/subarray-sum-equals-k/

from typing import List

# Smart Solution
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Smart Linear Solution
        prefix_map = {0: 1}

        # Maintain a counter which keeps track of sums accumulated so far
        running_sum = 0
        sub_array_count = 0

        # Iterate over the array once
        for element in nums:
            # Keep the running total
            running_sum += element
            
            # From the running total, check if we can cut a chunk of the prefixed arrays which sum upto how much amount should be deleted from current running total to obtain the value of k
            delta = running_sum - k
            sum_to_fetch = prefix_map.get(delta, 0)

            sub_array_count += sum_to_fetch

            prefix_map[running_sum] = 1 + prefix_map.get(running_sum, 0)
        
        return sub_array_count

# Trivial Solution
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)

        positions = []
        for i in range(n):
            running_sum = 0
            for j in range(i, n):
                running_sum += nums[j]
                if running_sum == k:
                    positions.append([i, j])
                elif running_sum > k:
                    break
        
        return len(positions)
                

