# https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/description/

from typing import List

# Classic Fixed size sliding window problem
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        window_size = k
        threshold = threshold * window_size
        running_sum = 0
        n = len(arr)

        L = 0
        result = 0

        # Go through the entire array once
        for R in range(n):
            # Get the current element in running sum
            running_sum += arr[R]

            if R - L  + 1 >= window_size:
                # If window threshold is reached, then check the condition
                if running_sum >= threshold:
                    result += 1

                # Adjust window by removing elements from the head of arr
                running_sum -= arr[L]
                L += 1
                
        return result