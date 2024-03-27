# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
from typing import List

class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        stack: List = []

        for element in s:
            if stack and stack[-1] == element:
                stack.pop()
            else:
                stack.append(element)
            
        return "".join(stack)