# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
from typing import List

# Slightly faster 
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "/", "*"]

        for token in tokens:
            if token in operators:
                op2 = stack.pop()
                op1 = stack.pop()

                if token == "+":
                    res = op1 + op2
                elif token == "-":
                    res = op1 - op2
                elif token == "*":
                    res = op1 * op2
                else:
                    res = int(op1 / op2)
                
                stack.append(res)
            else:
                stack.append(int(token))

        return stack[0]

# Slightly slower in terms of time (Because of the eval operation most likely)
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "/", "*"]

        for token in tokens:
            if token in operators:
                op2 = stack.pop()
                op1 = stack.pop()
                res = int(eval(f"{op1} {token} {op2}"))
                stack.append(res)
            else:
                stack.append(int(token))

        return stack[0]