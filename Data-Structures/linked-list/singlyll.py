class Node:
    def __init__(self, data=0, next=None):
        """
        Create a node for Singly Linked List
        """
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        """
        Initialize the head to always point to the head of the linked list
        """
        self.head = None

    def get(self, index: int):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        curr = self.head
        count = 0
        if self.head is None:
            print(-1)
        if index == 0:
            print(self.head.data)
        while curr:
            if count == index:
                print(curr.data)
            count += 1
            curr = curr.next
        print(-1)

    def insert_at_head(self, data):
        """Insert at head """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_tail(self, data):
        """Insert at the tail"""
        new_node = Node(data)
        # If there is no elements in the linked list then add it to the head
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node

    def add_at_index(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        new_node = Node(val)
        curr = self.head
        if index < 1:
            self.head = new_node
        else:
            count = 0
            prev = self.head
            while curr:
                count += 1
                if count == index:
                    new_node.next = prev.next
                    prev.next = new_node
                    break
                prev = curr.next
                curr = curr.next

            if count == index:
                curr.next = new_node
            else:
                print(-1)

    def delete_at_index(self, index: int):
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if self.head is None:
            print(-1)
        curr = self.head
        if index == 0:
            self.head = curr.next
        elif index < 0:
            print(-1)
        else:
            for i in range(index - 1):
                curr = curr.next
                if curr is None:
                    break
            if curr is None:
                return -1
            if curr.next is None:
                return -1

        next = curr.next.next
        curr.next = None
        curr.next = next

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
ll.get(1)
ll.printll()
ll.get(3)
ll.insert_at_head(15)
ll.insert_at_tail(20)
ll.printll()
ll.get(3)
ll.add_at_index(3)
ll.get(3)
ll.delete_at_index(3)
ll.printll()


"""
Insertion at the head is only done in O(1) time
DELETE operation can not be performed in O(1) time
"""
