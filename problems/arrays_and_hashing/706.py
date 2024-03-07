class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:
    def __init__(self):
        self.size = 10 ** 3
        self.elements = [Node(-1, -1) for x in range(self.size)]        

    def put(self, key: int, value: int) -> None:
        hash_position = key % self.size
        
        node = self.elements[hash_position]

        while True:
            # Modify if exists
            if key == node.key:
                node.value = value
                return        
            # Add if reached the end of chain  
            if not node.next:
                node.next = Node(key, value)
                return
            # Propagate till you reach the end of chain
            else:
                node = node.next
                

    def get(self, key: int) -> int:
        hash_position = key % self.size
        
        node = self.elements[hash_position]

        while True:
            # Modify if exists
            if key == node.key:
                return node.value
            # Add if reached the end of chain  
            if not node.next:
                break
            # Propagate till you reach the end of chain
            else:
                node = node.next

        return -1

    def remove(self, key: int) -> None:
        hash_position = key % self.size
        
        node = self.elements[hash_position]

        while True:
            
            if not node.next:
                return

            # Break the link if key exists
            if node.next.key == key:
                node.next = node.next.next
            
            
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)