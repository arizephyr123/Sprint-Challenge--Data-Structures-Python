class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def iterate_list(self, node):
        while node is not None:
            print("head",self.head.value ,"current", node.value)
            node = node.next_node

    def reverse_list(self, node, prev):
        if node is None:
            return
        if node.next_node is None:
            self.head = node
            self.head.next_node = prev
            return
        
        self.reverse_list(node.next_node, node)
        node.set_next(prev)

        if node == self.head:
            node.set_next(None)
        

# list = LinkedList()
# list.add_to_head(1)
# list.add_to_head(2)
# list.add_to_head(3)
# list.add_to_head(4)
# list.add_to_head(5)


# list.iterate_list(list.head)
# list.reverse_list(list.head, None)
# print("reversed")
# list.iterate_list(list.head)
