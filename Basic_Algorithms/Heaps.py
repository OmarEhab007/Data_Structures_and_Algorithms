# creat binary tree
from sympy import re


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, cur_node):
        if data < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
                self._insert(data, cur_node.left)
        elif data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                self._insert(data, cur_node.right)
        else:
            print("Value already in tree!")

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def search(self, data):
        if self.root is not None:
            return self._search(data, self.root)
        else:
            return False

    def _search(self, data, cur_node):
        if data == cur_node.data:
            return True
        elif data < cur_node.data and cur_node.left is not None:
            return self._search(data, cur_node.left)
        elif data > cur_node.data and cur_node.right is not None:
            return self._search(data, cur_node.right)
        return False

    def remove(self, data):
        # first find the node
        if self.root is not None:
            self.root = self._remove(data, self.root)

    def _remove(self, data, cur_node):
        if cur_node is None:
            return cur_node
        if data < cur_node.data:
            cur_node.left = self._remove(data, cur_node.left)
        elif data > cur_node.data:
            cur_node.right = self._remove(data, cur_node.right)
        else:
            if cur_node.left is None and cur_node.right is None:
                cur_node = None
            elif cur_node.left is None:
                cur_node = cur_node.right
            elif cur_node.right is None:
                cur_node = cur_node.left
            else:
                del_node = self.get_min(cur_node.right)
                cur_node.data = del_node.data
                cur_node.right = self._remove(del_node.data, cur_node.right)
        return cur_node

        """binary tree
        insert : O(log n)
        """
#_______________________________________________________#

        """
        ## Priority Queues

Like the name suggests,
a **priority queue** is similar to a regular queue,
except that each element in the queue has a priority associated with it.
A regular queue is a FIFO data structure, 
meaning that the first element to be added to the queue is also the first to be removed.

With a priority queue,
this order of removal is instead based on the priority. 
Depending on how we choose to set up the priority queue,
we either remove the element with the most priority,
or an element of the least priority. 
        """

class Heap:
    def __init__(self, initial_size=10):
        self.cbt = [None for _ in range(initial_size)]  # initialize arrays
        self.next_index = 0  # denotes next index where new element should go

    def insert(self, data):
        # insert element at the next index
        self.cbt[self.next_index] = data

        # heapify
        self._up_heapify()

        # increase index by 1
        self.next_index += 1

        # double the array and copy elements if next_index goes out of array bounds
        if self.next_index >= len(self.cbt):
            temp = self.cbt
            self.cbt = [None for _ in range(2 * len(self.cbt))]

            for index in range(self.next_index):
                self.cbt[index] = temp[index]

    def remove(self):
        if self.size() == 0:
            return None
        self.next_index -= 1

        to_remove = self.cbt[0]
        last_element = self.cbt[self.next_index]

        # place last element of the cbt at the root
        self.cbt[0] = last_element

        # we do not remove the elementm, rather we allow next `insert` operation to overwrite it
        self.cbt[self.next_index] = to_remove
        self._down_heapify()
        return to_remove

    def size(self):
        return self.next_index 

    def is_empty(self):
        return self.size() == 0

    def _up_heapify(self):
        # print("inside heapify")
        child_index = self.next_index

        while child_index >= 1:
            parent_index = (child_index - 1) // 2
            parent_element = self.cbt[parent_index]
            child_element = self.cbt[child_index]

            if parent_element > child_element:
                self.cbt[parent_index] = child_element
                self.cbt[child_index] = parent_element

                child_index = parent_index
            else:
                break

    def _down_heapify(self):
        parent_index = 0

        while parent_index < self.next_index:
            left_child_index = 2 * parent_index + 1
            right_child_index = 2 * parent_index + 2

            parent = self.cbt[parent_index]
            left_child = None
            right_child = None

            min_element = parent

            # check if left child exists
            if left_child_index < self.next_index:
                left_child = self.cbt[left_child_index]

            # check if right child exists
            if right_child_index < self.next_index:
                right_child = self.cbt[right_child_index]

            # compare with left child
            if left_child is not None:
                min_element = min(parent, left_child)

            # compare with right child
            if right_child is not None:
                min_element = min(right_child, min_element)

            # check if parent is rightly placed
            if min_element == parent:
                return

            if min_element == left_child:
                self.cbt[left_child_index] = parent
                self.cbt[parent_index] = min_element
                parent = left_child_index

            elif min_element == right_child:
                self.cbt[right_child_index] = parent
                self.cbt[parent_index] = min_element
                parent = right_child_index

    def get_minimum(self):
        # Returns the minimum element present in the heap
        if self.size() == 0:
            return None
        return self.cbt[0]

heap_size = 5
heap = Heap(heap_size)

elements = [1, 2, 3, 4, 1, 2]
for element in elements:
    heap.insert(element)
print('Inserted elements: {}'.format(elements))
print('heap array: {}'.format(heap.cbt))
print('size of heap: {}'.format(heap.size()))

for _ in range(4):
    print('Call remove: {}'.format(heap.remove()))
    print('heap array: {}'.format(heap.cbt))
    print('heap next_index: {}'.format(heap.next_index))
    print('size of heap: {}'.format(heap.size()))

print('Call get_minimum: {}'.format(heap.get_minimum()))

for _ in range(2):
    print('Call remove: {}'.format(heap.remove()))

print('size of heap: {}'.format(heap.size()))
print('Call remove: {}'.format(heap.remove()))
print('Call is_empty: {}'.format(heap.is_empty()))