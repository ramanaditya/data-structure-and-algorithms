from collections import deque


class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Operation:
    def __init__(self):
        self.queue = deque()
        self.list = []

    def insert(self, data, root, i, n):
        if i < n:
            temp = Node(data[i])
            root = temp
            root.left = self.insert(data, root.left, 2 * i + 1, n)
            root.right = self.insert(data, root.right, 2 * i + 2, n)
        return root

    def inorderTraversal(self, root):
        if root:
            self.inorderTraversal(root.left)
            if root.data:
                print(root.data, end=" ")
            self.inorderTraversal(root.right)
        return self.list


if __name__ == "__main__":
    op = Operation()
    root = Node()
    while True:
        print("Select the Operation : ")
        print(
            "1. Insert\n2. Inorder Traversal\n3. Pre Order Traversal\n4. Post Order Traversal\n5. Exit"
        )
        try:
            choice = int(input("Choice : "))
        except ValueError:
            print("\nThat was not a valid choice try again...\n")
        if choice == 1:
            # data = input("Enter the number to insert or null : ")
            data = ["1", "2", "3", "4", "5", "6"]
            root_temp = op.insert(data, root, 0, 6)
            root = root_temp
        if choice == 2:
            res = op.inorderTraversal(root)
            for i in res:
                print(i, end=" ")
            print()
        if choice == 5:
            quit()
