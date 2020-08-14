"""
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""

# Solutions

# Recursive Solution


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    Recursive Solution
    """

    def __init__(self):
        self.list = []

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root:
            self.inorderTraversal(root.left)
            if root.val:
                self.list.append(root.val)
            self.inorderTraversal(root.right)
        return self.list


# Runtime: 40 ms
# Memory Usage: 13.8 MB

# Iterative Solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    """
    Iterative Solution
    Time Complexity: O( n )
    Space Complexity: O( n )
    """

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # Base Case
        if not root:
            return

        stack = []
        res = []

        while root or stack:
            # Traverse to the extreme left
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            res.append(root.val)

            root = root.right

        return res


# Runtime: 20 ms, faster than 96.86% of Python3 online submissions
# Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions
