from linked_list import Linked_List


class Stack(object):
    def __init__(self, iterable=None):
        self._container = Linked_List(iterable)

    def push(self, val):
        """Use Linked List push method to add one Node to stack."""
        self._container.push(val)

    def pop(self):
        """Use Linked List pop() method to remove one from stack."""
        return self._container.pop()
