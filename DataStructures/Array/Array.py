class array_operation:
    """All the operations associated with list"""

    def __init__(self):
        self.array = []

    def get(self, index):
        if index < len(self.array):
            return self.array[index]
        return -1

    def insert_at_end(self, ele):
        self.array.append(ele)
        return

    def insert_at_index(self, ele, index):
        self.array.insert(index, ele)
        return

    def delete_at_end(self):
        if len(self.array) > 0:
            return self.array.pop()
        return -1

    def delete_ele(self, ele):
        res = self.search(ele)
        if res == -1:
            return res
        self.array.remove(ele)
        return res

    def delete_at_index(self, index):
        if index < len(self.array):
            return self.array.pop(index)
        return -1

    def search(self, key):
        for i in range(len(self.array)):
            if self.array[i] == key:
                return i
        return -1

    def display(self):
        for i in range(len(self.array)):
            print("{0} ".format(self.array[i]), end=" ")
        print()


if __name__ == "__main__":
    print("=================")
    print("List Operations")
    print("=================")
    op = array_operation()
    while True:
        print("Select the operation")
        print("1. Get the element at index")
        print("2. Search the element")
        print("3. Insert at end")
        print("4. Insert at index")
        print("5. Delete at end")
        print("6. Delete the element")
        print("7. Delete at Index")
        print("8. Display")
        print("9. Exit")
        print("Enter your choice : ", end="")
        choice = int(input())
        print()
        print("-------------------")
        if choice == 1:
            index = int(input("Enter the index : "))
            res = op.get(index - 1)
            if res == -1:
                print("List Index Out of range")
            else:
                print("Element at index : {} is {}".format(index, res))
        elif choice == 2:
            ele = int(input("Enter the element to search : "))
            res = op.search(ele)
            if res == -1:
                print("Element not found")
            else:
                print("Element {} found at index : {}".format(ele, res))
        elif choice == 3:
            ele = int(input("Enter the element to be inserted : "))
            op.insert_at_end(ele)
            op.display()
        elif choice == 4:
            ele = int(input("enter the element to insert : "))
            index = int(input("Enter the index : "))
            op.insert_at_index(ele, index)
            op.display()
        elif choice == 5:
            res = op.delete_at_end()
            if res == -1:
                print("List is Empty")
            else:
                print("Element {} has been deleted".format(res))
            op.display()
        elif choice == 6:
            ele = int(input("Enter the element to be deleted : "))
            res = op.delete_ele(ele)
            if res == -1:
                print("Element not present in the list")
            else:
                print("Element {} has been deleted from index : {}".format(ele, res))
            op.display()
        elif choice == 7:
            index = int(input("Enter the index to delete"))
            res = op.delete_at_index(index)
            if res == -1:
                print("List Index out of range")
            else:
                print(
                    "Elemetn : {} has been deleted from index : {}".format(res, index)
                )
        elif choice == 8:
            op.display()
        elif choice == 9:
            quit()
        else:
            print("Invalid Choice")
        print("-------------------")
