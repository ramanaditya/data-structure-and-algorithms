"""
10.2-2
Implement a stack using a singly linked list L. The operations PUSH and POP should still take O.1/ time.
"""


class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        """
        Pushing the data in the stack at top
        :param data: data
        :return: None
        """
        new_node = Node(data)
        print("Item Pushed :", end=" ")
        print(data)
        new_node.next = self.head
        self.head = new_node
        return

    def pop(self):
        """
        Deleting the top element of the stack
        :return: data
        """
        curr = self.head
        if not curr:
            return -1
        elif not curr.next:
            self.head = None
            return curr.data
        else:
            self.head = self.head.next
            return curr.data

    def display(self):
        """
        Displaying the elements in the stack
        :return: None
        """
        curr = self.head
        if not curr:
            print("Stack is underflow")
            return
        print("Stack is : ")
        print("top - > ", end="")
        while curr:
            print(curr.data, end=" - > ")
            curr = curr.next
        print("bottom")


if __name__ == "__main__":
    ll = LinkedList()
    while True:
        print("\n")
        print("Choice : ")
        print("1. Push")
        print("2. Pop")
        print("3. Display")
        print("4. Exit")
        choice = int(input("Enter your choice : "))
        if choice == 1:
            data = input("Enter the element to be pushed : ")
            ll.push(data)
        elif choice == 2:
            data = ll.pop()
            if data != -1:
                print("Item Popped :", end=" ")
                print(data)
            else:
                print("Stack is underflow")
        elif choice == 3:
            ll.display()
        elif choice == 4:
            print("Program exiting")
            exit()
        else:
            print("Invalid Choice Enter again")
