# https://leetcode.com/problems/largest-rectangle-in-histogram/
from typing import List

class Solution:
    def nearestSmallerLeft(self, heights: List[int], proxy:int|None = None) -> List[int]:
        if proxy is None: proxy = -1

        helper_stack = []
        nsl_indexes = []

        L, n = 0, len(heights)

        while L < n:
            this_element = heights[L]

            nsl_idx = proxy

            while len(helper_stack) and helper_stack[-1][0] > this_element:
                helper_stack.pop()

            if len(helper_stack):
                nsl_idx = helper_stack[-1][1]
            
            helper_stack.append((this_element, L))
            nsl_indexes.append(nsl_idx)
            L = L + 1
        
        return nsl_indexes

    def nearestSmallerRight(self, heights: List[int], proxy:int|None = None) -> List[int]:
        n = len(heights)
        
        if proxy is None: proxy = n
        R = n - 1
        
        helper_stack = []
        nsr_indexes = []

        while R > -1:
            this_element = heights[R]
            
            nsr_idx = proxy

            while len(helper_stack) and helper_stack[-1][0] >= this_element:
                helper_stack.pop()
            
            if len(helper_stack):
                nsr_idx = helper_stack[-1][1]
            
            nsr_indexes.append(nsr_idx)
            helper_stack.append((this_element, R))
            R -= 1
        
        nsr_indexes = nsr_indexes[::-1]

        return nsr_indexes

    def largestRectangleArea(self, heights: List[int]) -> int:

        # Find nearest smaller to left and nearest smaller to right elements
        nsl = self.nearestSmallerLeft(heights, -1)
        nsr = self.nearestSmallerRight(heights, len(heights))

        # Fid max area from the above
        max_area = -1
        for l, r, elem in zip(nsl, nsr, heights):
            a = (r - l -1) * elem
            if a > max_area:
                max_area = a
        
        return max_area