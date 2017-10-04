"""Implement the linked list data structure"""

class Node:
    """Node contains value and reference to the next node"""
    def __init__(self, val, next_node):
        self.val = val
        self.next = next_node

class LinkedList:
    """Linked list is useful for efficient add at the first"""
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_at_start(self, value):
        """Insert value into the head of the linked list"""
        if self.head is None:
            new_node = Node(value, None)
            self.head = new_node
        else:
            new_node = Node(value, self.head)
            self.head = new_node
            self.size += 1
    
    def insert_at_end(self, value):
        """Insert value into the tail of the linked list"""

    def traverse_list(self):
        """Traverse and print out the values in the list"""

    def remove_at_start(self):
        """remove the first node and return it"""

    def remove_at_end(self):
        """Traverse list and remove the tail node and return it"""
    
    def remove_value(self, value):
        """Traverse and remove the first encountered value"""

    def get_size(self):
        """TODO: Use getter, Get the size of the linked list"""
        return self.size
