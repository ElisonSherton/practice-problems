# https://leetcode.com/problems/3sum/description/
from typing import List

# Slightly better solution
# Sort the input array and things will become easier in terms of searching for triplets
class Solution:

    def twoSum(self, nums: List[int], k: int) -> set:

        possible_pairs = set()
        L = 0; R = len(nums) - 1
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

        return possible_pairs

    def threeSum(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        nums = sorted(nums) # -> nlogn
        triplets = set()

        # O(n squared)
        for i in range(n): # O(n)

            # Do not do repeat work if we have already obtained all the combinations for nums[i]
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Now do a two sum with target as k = 0 - nums[i]
            k = 0 - nums[i]

            # Search only to the right since we have already searched once for the presence of a triplet for all numbers on the left in previous passes
            search_array = nums[(i + 1):]
            possible_pairs = self.twoSum(search_array, k) # O(n)

            for p in possible_pairs:
                if nums[i] <= p[0]:
                    triplets.add((nums[i], p[0], p[1]))
                elif nums[i] >= p[1]:
                    triplets.add((p[0], p[1], nums[i]))
                else:
                    triplets.add((p[0], nums[i], p[1]))
        
        return triplets


# Working solution
class Solution:

    def twoSum(self, nums: List[int], k: int) -> List[List[int]]:

        search_set = {}
        for element in nums:
            search_set[element] = 1 + search_set.get(element, 0)

        possible_pairs = set()
        for element in nums:
            to_find = k - element
            if to_find in search_set:
                if (element == to_find):
                    if search_set[element] > 1:
                        possible_pairs.add((min(element, to_find), max(element, to_find)))
                else:
                    possible_pairs.add((min(element, to_find), max(element, to_find)))
        
        return possible_pairs

    def threeSum(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        triplets = set()

        for i in range(n):
            k = 0 - nums[i]
            search_array = nums[:i] + nums[(i + 1):]
            possible_pairs = self.twoSum(search_array, k)

            for p in possible_pairs:
                if nums[i] <= p[0]:
                    triplets.add((nums[i], p[0], p[1]))
                elif nums[i] >= p[1]:
                    triplets.add((p[0], p[1], nums[i]))
                else:
                    triplets.add((p[0], nums[i], p[1]))
        
        return triplets