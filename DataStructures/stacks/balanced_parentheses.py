from .stack import Stack

__author__ = "Omkar Pathak"


def balanced_parentheses(parentheses):
    """ Use a stack to check if a string of parentheses is balanced."""
    stack = Stack(len(parentheses))
    for parenthesis in parentheses:
        if parenthesis == "(":
            stack.push(parenthesis)
        elif parenthesis == ")":
            if stack.is_empty():
                return False
            stack.pop()
    return stack.is_empty()


if __name__ == "__main__":
    examples = ["((()))", "((())", "(()))"]
    print("Balanced parentheses demonstration:\n")
    for example in examples:
        print(example + ": " + str(balanced_parentheses(example)))
