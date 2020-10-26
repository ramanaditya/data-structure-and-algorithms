"""
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""

## Solutions

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """Recursive Solution"""

    def __init__(self):
        self.list = []

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root:
            if root.val:
                self.list.append(root.val)
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)
        return self.list


# Runtime: 40 ms
# Memory Usage: 13.9 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Iterative Solution
    Time Complexity: O( n )
    Space Complexity: O( n )
    """

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return
        stack = [root]
        res = []
        while stack:
            root = stack.pop()
            res.append(root.val)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
        return res


# Runtime: 20 ms, faster than 98.84% of Python3 online submissions
# Memory Usage: 13.8 MB, less than 67.62% of Python3 online submissions
