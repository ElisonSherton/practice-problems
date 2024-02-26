# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/description/

from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        l = len(arr)
        if l == 1:
            return [-1]
        elif l == 2:
            return [arr[1], -1]
        else:
            running_max = arr[-1]
            last, second_last = -1, running_max
            curr_element = arr[l - 2]
            for i in range(l - 3, -1, -1):
                running_max = max(curr_element, running_max)
                curr_element = arr[i]
                arr[i] = running_max
            arr[-1] = -1
            arr[-2] = second_last
        return arr