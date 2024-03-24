# https://leetcode.com/problems/4sum/

from typing import List

class Solution:

    def twoSum(self, nums: List[int], k: int) -> set:
        # print("In Twosum")
        possible_pairs = set()
        L = 0; R = len(nums) - 1
        # print(L, R)
        while R > L:
            curr_sum = nums[L] + nums[R]
            if curr_sum > k:
                R -= 1
            elif curr_sum < k:
                L += 1
            else:
                possible_pairs.add((nums[L], nums[R]))
                # Cant return directly since there can be more than 2 pairs which sum to the given target
                L += 1
        # print(L, R)

        return possible_pairs

    def threeSum(self, nums: List[int], target: int) -> set:
        # print("In Threesum")
        n = len(nums)
        triplets = set()

        # O(n squared)
        for i in range(n): # O(n)

            # Do not do repeat work if we have already obtained all the combinations for nums[i]
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Now do a two sum with target as k = 0 - nums[i]
            k = target - nums[i]

            # Search only to the right since we have already searched once for the presence of a triplet for all numbers on the left in previous passes
            search_array = nums[(i + 1):]
            # print(target, nums[i], k, search_array)
            possible_pairs = self.twoSum(search_array, k) # O(n)
            
            for p in possible_pairs:
                triplets.add((nums[i], p[0], p[1]))
        
        return triplets
    
    def fourSum(self, nums: List[int], target: int) -> set:

        n = len(nums)
        nums = sorted(nums)
        quadruplets = set()

        # O(n cubed)
        for i in range(n): # O(n)

            # Do not do repeat work if we have already obtained all the combinations for nums[i]
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Now do a two sum with target as k = 0 - nums[i]
            k = target - nums[i]

            # Search only to the right since we have already searched once for the presence of a triplet for all numbers on the left in previous passes
            search_array = nums[(i + 1):]
            # print("In Foursum")
            # print(nums[i], k, search_array)
            possible_triplets = self.threeSum(search_array, k) # O(nsquared)

            # Create quadruplets
            for p in possible_triplets:
                quadruplets.add((nums[i], p[0], p[1], p[2]))
        
        return quadruplets