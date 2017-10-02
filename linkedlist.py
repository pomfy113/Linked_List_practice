#!python

from __future__ import print_function


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data"""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node"""
        return 'Node({})'.format(repr(self.data))


class LinkedList(object):

    def __init__(self, iterable=None):
        """Initialize this linked list; append the given items, if any"""
        self.head = None
        self.tail = None
        if iterable:
            for item in iterable:
                self.append(item)

    def __repr__(self):
        """Return a string representation of this linked list"""
        return 'LinkedList({})'.format(self.as_list())

    def as_list(self):
        """Return a list of all items in this linked list"""
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            # result.append(current)
            current = current.next
        return result

    def is_empty(self):
        """Return True if this linked list is empty, or False"""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes"""
        # TODO: count number of items
        accum = 0
        counter = self.head

        while counter:
            counter = counter.next
            accum += 1
        return accum
        pass

    def append(self, item):
        """Insert the given item at the tail of this linked list"""
        # TODO: append given item
        new_node = Node(item)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
        pass

    def prepend(self, item):
        """Insert the given item at the head of this linked list"""
        # TODO: prepend given item
        new_node = Node(item)

        new_node.next = self.head
        self.head = new_node
        pass

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError"""
        # TODO: find given item and delete if found
        # if item == self.head.data:
        #     self.head = self.head.next
        # elif item == self.tail.data:
        #     print("That's a tail!")
        #     # for i in range(self.length()-1):
        #     #     self.tail = self.tail.next
        #     # self.tail.next = None
        # else:
        #     print("That's a body!")

        current = self.head
        previous = None

        while current:
            if current.data == item:
                if previous is None:
                    self.head = self.head.next
                else:
                    previous.next = None
            previous = current
            current = current.next

        pass

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality"""
        # TODO: find item where quality(item) is True
        counter = self.head

        while counter != None:
            if quality == counter.data:
                return counter.data
            else:
                counter = counter.next
        pass


def test_linked_list():
    ll = LinkedList()
    print(ll)
    ll.append('A')
    print(ll)
    ll.append('B')
    print(ll)
    ll.append('C')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    print(ll.length())

    ll.delete('A')
    print(ll)
    ll.delete('C')
    print(ll)
    ll.delete('B')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    print(ll.length())


if __name__ == '__main__':
    test_linked_list()
