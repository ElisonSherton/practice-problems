# https://leetcode.com/problems/daily-temperatures/

from typing import List

# Linear Time Complexity solution with monotonically decreasing stack
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        temperature_stack = []
        n = len(temperatures)
        answers = [0 for _ in range(n)]

        for idx, element in enumerate(temperatures):
            if idx == 0:
                temperature_stack.append((element, idx))
                continue
            
            while True:
                # If stack is empty then break
                if len(temperature_stack) == 0: 
                    break

                # Peek at the topmost element
                t, t_idx = temperature_stack[-1]
                
                # If current element is higher, then set the answers for the last element on top of stack
                if element > t:
                    answers[t_idx] = idx - t_idx
                    temperature_stack.pop()
                else:
                    break
                    
            # Get the current element on the stack
            temperature_stack.append((element, idx))
                    
        return answers    

# Quadratic Complexity Solution
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        L = 0
        n = len(temperatures)
        answers = []

        # O(n**2) Solution
        while L < n:
            curr = temperatures[L]
            R = L + 1
            while R < n and curr >= temperatures[R]:
                R = R + 1
            if R == n:
                answers.append(0)
            else:
                answers.append(R - L)
            L = L + 1
        
        return answers
            

                
