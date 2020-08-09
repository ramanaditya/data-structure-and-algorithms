class Node:
    def __init__(self, data=0, next=None):
        """
        Create a node for Singly Linked List
        """
        self.data = data
        self.next = next


class LinkedList:
    """Operations associated with the Linked List"""

    def __init__(self):
        """
        Initialize the head to always point to the head of the linked list
        """
        self.head = None

    def search(self, data):
        """To search the given data in the Linked list and find it's first occurrence, if it is not present return -1"""
        curr = self.head
        index = 0
        while curr:
            if curr.data == data:
                return index
            index += 1
            curr = curr.next
        return -1

    def get(self, index: int):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        curr = self.head
        count = 0
        if self.head is None:
            return -1
        if index == 0:
            return self.head.data
        while curr:
            if count == index:
                return curr.data
            count += 1
            curr = curr.next
        return -1

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
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked
        list, the node will be appended to the end of linked list. If index is greater than the length, the node will
        not be inserted.
        """
        index -= 1
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        if index < 1:
            new_node.next = self.head
            self.head = new_node
            return
        else:
            count = 0
            prev = self.head
            while curr:
                count += 1
                if count == index:
                    new_node.next = curr.next
                    curr.next = new_node
                    return
                prev = curr
                curr = curr.next
            if count == index:
                curr.next = new_node
                return
            else:
                prev.next = new_node
                return

    def delete_head(self):
        if not self.head:
            return -1
        else:
            value = self.head.data
            temp = self.head.next
            self.head = None
            self.head = temp
            return value

    def delete_tail(self):
        if not self.head:
            return -1
        else:
            curr = self.head
            if not curr.next:
                value = curr.data
                self.head = None
                return value
            while curr.next.next:
                curr = curr.next
            value = curr.next.data
            curr.next = None
            return value

    def delete_at_index(self, index: int):
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        index -= 1
        if self.head is None:
            return -1
        curr = self.head
        if index == 0:
            value = curr.data
            self.head = curr.next
            return value
        elif index < 0:
            return -1
        else:
            for i in range(index - 1):
                curr = curr.next
                if curr is None:
                    break
            if curr is None:
                return -1
            if curr.next is None:
                return -1
        value = curr.data
        next = curr.next.next
        curr.next = None
        curr.next = next
        return value

    def printll(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("/")


if __name__ == "__main__":
    ll = LinkedList()
    while True:
        print("\n======================")
        print("Linked List Operations")
        print("======================")
        print("Select the operation")
        print("1. Get the Node")
        print("2. Search")
        print("3. Insert at Head")
        print("4. Insert at Tail")
        print("5. Insert at Index")
        print("6. Delete at head")
        print("7. Delete at Tail")
        print("8. Delete at Index")
        print("9. Display Linked List")
        print("10. Exit")
        choice = int(input("Choice : "))
        print("\n---------------")
        if choice == 1:
            index = int(input("Enter the index to get the value of the node : "))
            node = ll.get(index)
            if node == -1:
                print("Node Does not exist at index {}".format(index))
            else:
                print("node '{}' is present at index : {}".format(node, index))
        elif choice == 2:
            val = int(input("Enter the value to be searched : "))
            index = ll.search(val)
            if index == -1:
                print("node '{}' is not present".format(val))
            else:
                print("node '{}' is present at index : {}".format(val, index))

        elif choice == 3:
            node = int(input("Enter the val of node to be inserted : "))
            ll.insert_at_head(node)
            ll.printll()
        elif choice == 4:
            node = int(input("Enter the val of node to be inserted : "))
            ll.insert_at_tail(node)
            ll.printll()
        elif choice == 5:
            index = int(input("Enter the index at which node will be inserted : "))
            node = int(input("Enter the val of node to be inserted : "))
            ll.add_at_index(index, node)
            ll.printll()
        elif choice == 6:
            value = ll.delete_head()
            if value == -1:
                print("Linked List does not exist")
            else:
                print("node '{}' has been deleted from head".format(value))
            ll.printll()
        elif choice == 7:
            value = ll.delete_tail()
            if value == -1:
                print("Linked List does not exist")
            else:
                print("node '{}' has been deleted from tail".format(value))
            ll.printll()
        elif choice == 8:
            index = int(input("Enter the index to delete the node : "))
            value = ll.delete_at_index(index)
            if value == -1:
                print("Node does not exist")
            else:
                print("node '{}' has been deleted at index {}".format(value, index))
            ll.printll()
        elif choice == 9:
            ll.printll()
        elif choice == 10:
            quit()
        else:
            print("Invalid Choice")
        print("---------------")
