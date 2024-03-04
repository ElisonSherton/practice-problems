# https://leetcode.com/problems/next-greater-element-i/

from typing import List

# Efficient Solution
# Can be made more efficient by only finding the next greatest for elements in nums1, but this is still fine; that would only need minor changes to the for loop
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        next_greatest_map = {}
        # Maintain a monotonically decreasing stack
        interim_stack = [nums2[0]]

        # Iterate over all elements of nums2 and get the next largest for every element
        for i in range(1, len(nums2)):
            curr_element = nums2[i]

            # Pop elements of stack until the curr element wherever there is a greater element encountered
            while len(interim_stack) > 0:
                element = interim_stack[-1]
                if curr_element > element:
                    next_greatest_map[element] = curr_element
                    interim_stack = interim_stack[:-1]
                    if not interim_stack: interim_stack = [curr_element]
                else:
                    interim_stack.append(curr_element)
                    break
        
        # Finally, for the elements which remain in the interim stack, no greater element to the right was observed hence, set their values to -1
        for element in interim_stack:
            next_greatest_map[element] = -1
                
        return [next_greatest_map[x] for x in nums1]


# Very Trivial Solution O(n2**2 + n1)
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Trivial Solution
        next_greater_map = {}

        for i in range(len(nums2)):
            query_element = nums2[i]
            for j in range(i + 1, len(nums2)):
                if nums2[j] > query_element:
                    next_greater_map[query_element] = nums2[j]
                    break
            if not query_element in next_greater_map:
                next_greater_map[query_element] = -1
        
        return [next_greater_map[x] for x in nums1]
