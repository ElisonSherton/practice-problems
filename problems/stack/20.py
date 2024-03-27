# https://leetcode.com/problems/valid-parentheses/description/

from typing import List

class Solution:
    def isValid(self, inp: str) -> bool:
        
        s: List = []
        open_count, close_count = 0, 0

        for element in inp:
            if element == "}":
                close_count += 1
                if s and s[-1] == "{":
                    s.pop()
            elif element == ")":
                close_count += 1
                if s and s[-1] == "(":
                    s.pop()
            elif element == "]":
                close_count += 1
                if s and s[-1] == "[":
                    s.pop()
            else:
                open_count += 1
                s.append(element)
        
        if len(s) > 0 or open_count != close_count:
            return False
        
        return True