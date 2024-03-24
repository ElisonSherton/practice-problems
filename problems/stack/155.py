# https://leetcode.com/problems/min-stack/description/

# Working solution
class MinStack:

    def __init__(self):
        # Maintain a separate stack for minimum at each position
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.min_stack.append(val)
        else:
            curr_min = self.min_stack[-1]
            if val < curr_min:
                self.min_stack.append(val)
            else:
                self.min_stack.append(curr_min)        
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()