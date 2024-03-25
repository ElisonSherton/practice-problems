# https://leetcode.com/problems/baseball-game/description/
from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        num_stack: List = []

        for element in operations:
            if element == "C":
                num_stack.pop()
            elif element == "D":
                o1 = num_stack.pop()
                num_stack.append(o1)
                num_stack.append(2 * o1)
            elif element == "+":
                o2, o1 = num_stack.pop(), num_stack.pop()
                num_stack.append(o1)
                num_stack.append(o2)
                num_stack.append(o1 + o2)
            else:
                num_stack.append(int(element))
        
        total = 0
        while len(num_stack):
            total += num_stack.pop()
        
        return total