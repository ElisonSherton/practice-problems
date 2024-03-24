# https://leetcode.com/explore/learn/card/queue-stack/228/first-in-first-out-data-structure/1337/

class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [0 for _ in range(k)]
        self.head = 0
        self.tail = 0
        self.size = k
        self.is_full = False
        self.is_empty = True

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            self.is_empty = False
            
            self.q[self.tail] = value
            self.is_empty = False
            
            self.tail = (self.tail + 1) % self.size
            if self.tail == self.head:
                self.is_full = True
            return True
        return False

    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.is_full = False
            self.q[self.head] = 0
            self.head = (self.head + 1) % self.size
            if self.head - self.tail == 0:
                self.is_empty = True
            return True
        return False
               

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[(self.tail - 1) % self.size]

    def isEmpty(self) -> bool:
        return self.is_empty

    def isFull(self) -> bool:
        return self.is_full
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()