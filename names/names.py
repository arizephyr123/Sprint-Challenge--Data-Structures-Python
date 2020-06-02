import time
import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# runtime: 5.7142s
# runtime complexity: O(n^2)
# for name_1 in names_1: # O(n)
#     for name_2 in names_2: # O(n)
#         if name_1 == name_2: 
#             duplicates.append(name_1) # O(1)
#=============
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.count = 1

def insert(root, value):
    if not root:
        return BSTNode(value)
    elif root.value == value:
        root.count += 1
    elif value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)

    return root

def create(seq):
    root = None
    for word in seq:
        root = insert(root, word)

    return root

def search(root, word, depth=1):
    if not root:
        return 
    elif root.value == word:
        return depth, root.count
    elif word < root.value:
        return search(root.left, word, depth + 1)
    else:
        return search(root.right, word, depth + 1)

# def print_tree(root):
#     if root:
#         print_tree(root.left)
#         print(root)
#         print_tree(root.right)


# create BStree containing names_1
names_tree = create(names_1) 

# search for names_2 names_tree
## add to duplicates list
for name in names_2:
    if search(names_tree, name) is not None:
        duplicates.append(name)
#==============
end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
