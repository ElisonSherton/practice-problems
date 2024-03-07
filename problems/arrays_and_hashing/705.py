# https://leetcode.com/problems/design-hashset/description/

# Working solution -> Better one with chaining and considering max points of 10**4
class MyHashSet:
    def __init__(self):
        self.elements = [[]] * (10 ** 4)
        self.divisor = 10 ** 4

    def add(self, key: int) -> None:
        insertion_point = key // self.divisor
        
        contains = False
        for element in self.elements[insertion_point]:
            if element == key: contains = True
        
        if not contains:
            self.elements[insertion_point].append(key)

    def remove(self, key: int) -> None:

        removal_point = key // self.divisor
        
        new_chain = []
        for element in self.elements[removal_point]:
            if element != key: new_chain.append(element) 

        self.elements[removal_point] = new_chain

    def contains(self, key: int) -> bool:
        search_point = key // self.divisor
        
        for element in self.elements[search_point]:
            if element == key: return True

        return False


# WIP
class MyHashSet:
    def __init__(self):
        self.elements = []
        self.max = -1
        self.min = 10 ** 7
        self.initialized = True

    def add(self, key: int) -> None:
        if self.initialized:
            self.max = self.min = key
            self.elements.append(key)
            self.initialized = False

        if (key == self.max) or (key == self.min):
            return
        elif key > self.max:
            self.max = key
            # Add to the end
            self.elements.append(key) 
        elif key < self.min:
            # Add to the start
            self.min = key
            self.elements = [key] + self.elements
        else:
            # Figure out where to add
            new_element_list = []
            for element in self.elements:
                if key < element:
                    new_element_list.append(key)
                new_element_list.append(element)
            self.elements = new_element_list

    def remove(self, key: int) -> None:
        if (key > self.max) or (key < self.min):
            return
        else:
            new_element_list = []
            for element in self.elements:
                if key != element:
                    new_element_list.append(element)
            self.elements = new_element_list

    def contains(self, key: int) -> bool:
        # Binary search
        # print(key, self.elements)
        if (key > self.max) or (key < self.min):
            return False
        else:
            low = 0
            high = len(self.elements) - 1

            if len(self.elements) == 1:
                return self.elements[0] == key
            elif len(self.elements) == 2:
                return (self.elements[0] == key) or (self.elements[1] == key)

            while low <= high:
                mid = (low + high) // 2
                # print(low, high, mid, key)
                # print(self.elements[low], self.elements[high], self.elements[mid], key)
                if self.elements[mid] < key:
                    low = mid
                elif self.elements[mid] > key:
                    high = mid
                elif self.elements[mid] == key:
                    return True
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)


# Trivial Solution
class MyHashSet:
    def __init__(self):
        self.current_order = 10
        self.hashset = [0] * (10**6 + 1)
        self.divisor = 10**6 + 2

    def get_order_of_mag(self, num):
        o = 0
        while num > 0:
            o += 1
            num = num // 10
        return (10 ** o)
    
    def reset_map(self, order):
        new_hashset = [0] * order
        for idx, element in enumerate(self.hashset):
            new_hashset[idx] = element
        self.hashset = new_hashset

    def add(self, key: int) -> None:
        o = self.get_order_of_mag(key)
        if o > self.current_order:
            self.reset_map(o)        
        self.hashset[key % self.divisor] = 1

    def remove(self, key: int) -> None:
        self.hashset[key % self.divisor] = 0

    def contains(self, key: int) -> bool:
        if self.hashset[key % self.divisor]:
            return True
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)