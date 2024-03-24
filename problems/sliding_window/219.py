# https://leetcode.com/problems/contains-duplicate-ii/description/
from typing import List

# Fixed size sliding window solution
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        distinct_elements = set()
        window_size = k + 1

        window = set()
        # Initialize the window
        for idx, element in enumerate(nums[:window_size]):
            if element in window:
                return True
            else:
                window.add(element)

        # Fixed size sliding window iteration
        for idx in range(window_size, len(nums)):
            window.remove(nums[idx - window_size])
            curr = nums[idx]
            if curr in window:
                return True
            window.add(curr)
        
        return False


# Using Hashmap
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        positions_hashmap = {}
        encountered_duplicates = False

        for idx, element in enumerate(nums):
            if element in positions_hashmap:
                first_occurence = positions_hashmap[element][0]
                positions_hashmap[element].append(idx)
                encountered_duplicates = True
            else:
                positions_hashmap[element] = [idx]
        
        if not encountered_duplicates: return False

        for v in positions_hashmap.values():
            for p, c in zip(v[:-1], v[1:]):
                if c - p <= k: return True

        return False
        