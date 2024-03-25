# https://leetcode.com/problems/validate-stack-sequences/description/
from typing import List

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        # By default push the first element on the stack
        current_stack = [pushed[0]]
        n = len(pushed)
        push_ptr = 1
        pop_ptr = 0

        while True:
            # Complete all the operations in push and pop
            if push_ptr < n or pop_ptr < n:
                # If the top of stack has same element as the element which pop pointer points to, pop the element
                if current_stack[-1] == popped[pop_ptr]:
                    current_stack.pop()
                    pop_ptr += 1
                    # If after popping, the stack becomes empty, push the next element in the push ptr on the stack
                    if not current_stack and push_ptr < n:
                        current_stack.append(pushed[push_ptr])
                        push_ptr += 1
                else:
                    # If the top of stack doesn't have same elment which the pop pointer points to, push the next element from push sequence to the stack
                    if push_ptr < n:
                        current_stack.append(pushed[push_ptr])
                        push_ptr += 1
                    # If you have reached the end of push stack, that means the popping is not complete and cannot proceed as well because topmost element is not equal to the element to be popped at this time and there is no more pushing to do
                    else:
                        return False
            else:
                return current_stack == []