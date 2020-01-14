"""
Can you implement the dynamic-set operation INSERT on a singly linked list in O(1) time? How about DELETE?
"""


class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    """Insertion at the head is done in O(1) time"""

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node

    def printll(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("/")


ll = LinkedList()
ll.insert_at_tail(40)
ll.insert_at_head(5)
ll.insert_at_head(10)
ll.printll()
ll.insert_at_head(15)
ll.insert_at_tail(20)
ll.printll()


"""
Insertion at the head is only done in O(1) time
DELETE operation can not be performed in O(1) time
"""
