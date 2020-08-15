"""
# 145. [Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/)
Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""

# Solutions

"""Recursive"""
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.list = []

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root:
            self.postorderTraversal(root.left)
            self.postorderTraversal(root.right)
            if root.val:
                self.list.append(root.val)
        return self.list


# Runtime: 36 ms
# Memory Usage: 14 MB

"""Iterative"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


from collections import deque


class Solution:
    """
    Iterative Solution
    Time Complexity: O( n )
    Space Complexity: O( n )
    """

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return

        stack = []
        res = deque()

        while root or stack:
            if root:
                stack.append(root)
                res.appendleft(root.val)
                root = root.right
            else:
                root = stack.pop()
                root = root.left

        return res


# Runtime: 20 ms, faster than 98.81% of Python3 online submissions
# Memory Usage: 13.7 MB, less than 84.50% of Python3 online submissions


class Solution:
    """
    Iterative Solution
    Time Complexity: O( n )
    Space Complexity: O( n )
    """

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return

        stack = [root]
        res = []

        while stack:
            root = stack.pop()
            res.append(root.val)
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)

        return res[::-1]


# Runtime: 24 ms, faster than 94.20% of Python3 online submissions
# Memory Usage: 13.7 MB, less than 91.81% of Python3 online submissions
