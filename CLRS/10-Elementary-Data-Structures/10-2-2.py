"""
10.2-2
Implement a stack using a singly linked list L. The operations PUSH and POP should still take O.1/ time.
"""

SIZE = 5


class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.SIZE_COUNT = 0

    def push(self, data):
        if SIZE == self.SIZE_COUNT - 1:
            print("Stack is overflow")
            return
        else:
            new_node = Node(data)
            print("Item Pushed :", end=" ")
            print(data)
            new_node.next = self.head
            self.head = new_node
            self.SIZE_COUNT += 1

    def pop(self):
        curr = self.head
        if not curr:
            print("Stack is underflow")
        elif not curr.next:
            print("Item Popped :", end=" ")
            print(curr.data)
            self.head = None
        else:
            print("Item Popped :", end=" ")
            print(curr.data)
            self.head = self.head.next

    def printll(self):
        curr = self.head
        if not curr:
            print("Stack is underflow")
            return
        print("Stack is : ")
        while curr:
            print(curr.data)
            curr = curr.next


ll = LinkedList()
ll.push(5)
ll.push(10)
ll.push(15)
ll.push(20)
ll.push(25)
ll.printll()
ll.pop()
ll.pop()
ll.pop()
ll.pop()
ll.pop()
ll.printll()
