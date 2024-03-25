# https://leetcode.com/problems/removing-stars-from-a-string/description/

from typing import List

class Solution:
    def removeStars(self, s: str) -> str:
        
        string_stack: List = []

        for element in s:
            if element == "*":
                string_stack.pop()
            else:
                string_stack.append(element)
        
        return "".join(string_stack)