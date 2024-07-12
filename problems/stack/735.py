# https://leetcode.com/problems/asteroid-collision/
from typing import List

# Correct Solution
class Solution:

    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        state = []
        L = 0
        n = len(asteroids)
        top = None

        while L < n:
            element = asteroids[L]

            # Just push the first element as is on the stack
            if L == 0:
                state.append(element)
                L = L + 1
                continue
            
            # As opposed to the different solution, if asteroids are drifting apart, that is no issue, only if they are approaching each other, then it becomes an issue
            while state and (element < 0 and state[-1] > 0):
                top = state[-1]
                if abs(top) == abs(element):
                    state.pop()
                    element = None
                    break
                elif abs(top) > abs(element):
                    element = None
                    break
                else:
                    state.pop()

            if element:
                state.append(element)
            
            L = L + 1
        
        return state

# Misunderstood the question
class DifferentSolution:

    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        state = []
        L = 0
        n = len(asteroids)
        top = None

        while L < n:
            element = asteroids[L]

            # Just push the first element as is on the stack
            if L == 0:
                state.append(element)
                L = L + 1
                continue
            
            # Keep popping and comparing till both the top of state and the current element are headed in the same direction
            while state and (element > 0 and state[-1] < 0) or (element < 0 and state[-1] > 0):
                top = state[-1]
                if abs(top) == abs(element):
                    state.pop()
                    element = None
                    break
                elif abs(top) > abs(element):
                    element = None
                    break
                else:
                    state.pop()
                    
            if element:
                state.append(element)
            
            L = L + 1
        
        return state