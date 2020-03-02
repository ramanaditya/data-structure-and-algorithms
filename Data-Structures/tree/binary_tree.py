class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Operation:
    def __init__(self):
        self.queue = []
        self.list = []

    def insert(self, root, data):
        if len(self.queue) == 0:
            root = Node(data)
            self.queue.append(root)
        else:
            temp = self.queue[0]
            if temp.left is not None:
                root.left = Node(data)
                self.queue.append(temp.left)
            elif temp.right is not None:
                root.right = Node(data)
                self.queue.append(temp.right)
            self.queue.pop(0)
        return root

    def inorderTraversal(self, root):
        if root:
            self.inorderTraversal(root.left)
            if root.data:
                self.list.append(root.data)
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
            data = input("Enter the number to insert or null : ")
            root = op.insert(root, data)
            print(root.data)
        if choice == 2:
            res = op.inorderTraversal(root)
            for i in res:
                print(i)
        if choice == 5:
            break
