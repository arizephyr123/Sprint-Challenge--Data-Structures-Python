"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


def iterate_list(node):
    while node is not None:
        print(node.value)
        node = node.next


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node  # remember head
        self.tail = node  # remember tail
        self.length = 1 if node is not None else 0  # like ternary

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):
        # print("in add_to_head", value)
        # wrap the given value in a list node
        new_node = ListNode(value, None, None)  # made new node
        self.length += 1  # because adding a node
        # handle if list has a head
        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        # handle if node has no head
        else:
            self.head = new_node
            self.tail = new_node  # because new_node is first, last, only current node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        value = self.head.value
        # print("in remove_from_head", value)
        # self.length -= 1  # because removing a node
        self.delete(self.head)
        return value

    """Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        # print("in add_to_tail", value)
        new_node = ListNode(value)
        self.length += 1  # because adding a node
        # there is a tail
        if self.tail:
            self.tail.next = new_node  # set tail to new_node instead of None
            new_node.prev = self.tail  # set previous tail to new_node prev
        # there is no tail
        else:
            self.tail = new_node  # if no tail, no head because empty list
            self.head = new_node

        self.tail = new_node

    """Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):

        value = self.tail.value  # grabbing value before deleting to return
        # print("in remove_from_tail", value)
        # could use following, but doing hard way for practice
        # self.delete(self.tail)

        # if 0 nodes, nothing to remove
        if not self.tail:
            return

        # if head and tail are same (1 node)
        elif self.head == self.tail:
            self.head = None
            self.tail = None

        # if more than 1 node
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        self.length -= 1
        return value

    """Removes the input node from its current spot in the
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        # print("in move_to_front", node.value)
        value = node.value
        self.delete(node)  # removes from current spot
        self.add_to_head(value)  # inserts as head
        # self.add_to_head(node)  # inserts as head

    """Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        # print("in move_to_end", node.value)
        value = node.value
        self.delete(node)
        self.add_to_tail(value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        # print("in delete", node.value)

        # if list is empty
        if not self.head:
            print("nothing to delete")
            return

        self.length -= 1  # decrement list lenth by one that is removed
        # if list has just one item
        # if self.head == self.tail == None
        if self.head == self.tail:
            self.head = None
            self.tail = None

        # we have at least 2 nodes, and the node we want to delete is the head
        if node == self.head:
            self.head = node.next
            self.tail.prev = None
            # node.delete()

        # we have at least 2 nodes, and the node we want to delete is the tail
        if node == self.tail:
            self.tail = node.prev
            self.tail.next = None
            # node.delete()

        else:
            node.delete()

    """Returns the highest value currently in the list"""

    def get_max(self):
        # print(" in get_max")

        highest_value = self.head.value
        current_node = self.head

        # walk through entire list
        while current_node != None:
            # keep track of the max value we've found
            if current_node.value > highest_value:
                highest_value = current_node.value
            # keep iterating through list
            current_node = current_node.next
        return highest_value

    # ====== from lecture =====
    '''How do you find and return the middle node of a singly linked list in one pass? You do not have access to the length of the list. If the list is even, you should return the first of the two "middle" nodes. You may not store the nodes in another data structure.'''

    def find_middle(self):
        middle = self.head
        end = self.head

        while end.next != None and end.next.next != None:
            end = end.next.next
            middle = middle.next

        print(middle.value, end.value)
        return middle


'''
does this work??
def find_middle_alt(self):
    middle_a = self.head
    middle_b = self.head

    while middle_b != None:
        middle_a = middle_b
        middle_b = middle_a.next
    return middle_a
'''

# head should now be tail
# tail should now be head
# no recursion, no other data structures


# def reverse_list(self):
#     pass


# my_node = ListNode(12)
# my_node.insert_after(25)
# my_node.insert_after(100)
# my_node.next.insert_after(99)

# iterate_list(my_node)

# dllist = DoublyLinkedList()

# dllist.add_to_head(1)
# print(dllist.tail.value)
# dllist.add_to_tail(1)
# dllist.add_to_tail(2)
# dllist.add_to_tail(3)
# dllist.add_to_tail(4)
# dllist.add_to_tail(5)
# print(dllist.tail.value)
# print(dllist.tail.prev.value)
# print(dllist.head.value)
# iterate_list(dllist.head)
# dllist.delete(dllist.head.next)
# iterate_list(dllist.head)

# dllist.find_middle()
