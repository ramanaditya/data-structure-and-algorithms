"""
12.1-4
Give recursive algorithms that perform preorder and postorder tree walks in O(n) time on a tree of nodes.
"""


class Node:
    """Node of the tree"""

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def postorderTraversal(root):
    """Post Order Traversal, Recursive"""
    res = []
    if not root:
        return res
    else:
        res += postorderTraversal(root.left)
        res += postorderTraversal(root.right)
        res.append(root.data)
    return res


def preorderTraversal(root, res=[]):
    """Pre Order Traversal, Recursive"""
    if not root:
        return res
    else:
        res.append(root.data)
        preorderTraversal(root.left, res)
        preorderTraversal(root.right, res)
    return res


if __name__ == "__main__":
    """
            1
           / \
          2   3
         / \  /
        4  5  6
    """
    root = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6)))
    post_list = []
    print("Post order Traversal")
    post_list = postorderTraversal(root)
    for i in post_list:
        print(i, end=" ")
    print()
    print("Pre order Traversal")
    pre_list = []
    pre_list = preorderTraversal(root)
    for i in pre_list:
        print(i, end=" ")
    print()
