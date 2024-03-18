# https://leetcode.com/problems/rotate-array/description/

from typing import List

# Improvement: O(1) space, O(3 * n) time
class Solution:

    def reverse(self, nums: List[int], l: int, r: int) -> None:
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1; r -= 1


    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        k = k % n

        if k == 0: return
        
        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)

# Improvement: O(k) space, O(n) time
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Avoid rotations unnecessarily (i.e. those which get the string back to it's original state)
        n = len(nums)
        k = k % n

        # If no rotations to be made, just return
        if k == 0: return
        
        # Keep a window of size k to facilitate the rotation
        window = []
        r = n - k
        for idx, element in enumerate(range(r, n)):
            window.append(nums[idx])
            nums[idx] = nums[element]

        # Once window reaches size k, now, just start substituting stuff back in the original array
        for L in range(len(window), n):
            window_idx = L % k
            nums[L], window[window_idx] = window[window_idx], nums[L]
            

# Working solution O(n) space, O(n) time
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        k = k % n
        
        window = []

        r = n - k
        for idx, element in enumerate(range(r, n)):
            window.append(nums[idx])
            nums[idx] = nums[element]

        for L in range(len(window), n):
            window.append(nums[L])
            nums[L] = window[L - k]
                
        return nums