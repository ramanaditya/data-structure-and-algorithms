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


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        from collections import deque

        stack = []
        res = deque()
        while root or len(stack) > 0:
            if root:
                stack.append(root)
                res.appendleft(root.val)
                root = root.right
            else:
                node = stack.pop()
                root = node.left
        return res


# Runtime: 28 ms, faster than 65.91% of Python3 online submissions
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions
