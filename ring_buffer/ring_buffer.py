import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        # self.data = [None for el in range(self.capacity)]
        self.data = [None]*capacity
        self.tracker = -1
    

    # The `append` method adds the given element to the buffer. 
    def append(self, item):
        self.tracker += 1
        position = self.tracker % self.capacity
        self.data[position] = item

    
    # The `get` method returns all of the elements in the buffer in a list in their given order. It should not return any `None` values
    def get(self):
        items = [el for el in self.data if el is not None]
        return items
                
    

# buffer = RingBuffer(5)
# buffer.append('a')
# print("buffer.get", buffer.get())
# buffer.append('b')
# buffer.append('c')
# buffer.append('d')
# buffer.append('e')
# buffer.append('f')
# buffer.append('g')
# buffer.append('h')
# buffer.append('i')

# print("buffer.get", buffer.get())

