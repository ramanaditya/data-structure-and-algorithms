class Stack:
    """
    In python, stack doesn't make any sense as list has all inbuilt methods for the same
    But algorithm works as demonstrated below
    """
    def __init__(self, size):
        self.stack = []
        self.size = size  # fixed sized stack
        self.top = -1  # index of stack

    def push(self, ele) -> None:
        if not self.overflow():
            self.top += 1
            self.stack.append(ele)
        else:
            print("Stack Overflow")

    def pop(self) -> int:
        if not self.underflow():
            self.top -= 1
            return self.stack.pop()
        print("Stack Underflow")
        return -1

    def underflow(self) -> bool:
        if self.top == -1:
            return True
        return False

    def overflow(self):
        if self.top == self.size - 1:
            return True
        return False

    def get_top(self):
        if self.underflow() or self.overflow():
            return -1
        return self.stack[self.top]

    def display(self):
        print("TOP <--", end=" ")
        top = self.top
        while top >= 0:
            print(f"{self.stack[top]} <--", end=" ")
            top -= 1
        print("/")


if __name__ == "__main__":
    print("=================")
    print("Stack Operations")
    print("=================")
    size = int(input("Enter the size of Stack: "))
    stack = Stack(size)

    while True:
        print("Select the operation")
        print("1. Push into Stack")
        print("2. Pop out of stack")
        print("3. Check Underflow")
        print("4. Check Overflow")
        print("5. Get top of the stack")
        print("6. Display")
        print("7. Exit")
        print("Enter your choice : ", end="")
        choice = int(input())
        print()
        print("-------------------")
        if choice == 1:
            element = input("Enter the element to push: ")
            stack.push(element)
        elif choice == 2:
            element = stack.pop()
            if element:
                pass
            else:
                print(f"Removed Element is: {element}")
        elif choice == 3:
            print(f"Underflow: {stack.underflow()}")
        elif choice == 4:
            print(f"Overflow: {stack.overflow()}")
        elif choice == 5:
            print(f"Element at the top of stack: {stack.get_top()}")
        elif choice == 6:
            stack.display()
            print("-------------------")
            continue
        elif choice == 7:
            quit()
        else:
            print("Invalid Choice")
        stack.display()
        print("-------------------")