"""
[872. Leaf-Similar Trees](https://leetcode.com/problems/leaf-similar-trees/)
Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.



Note:
Both of the given trees will have between 1 and 100 nodes.
"""


# Solutions

# Recursive Solution

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.first = []
        self.second = []

    def check1(self, root1):
        if not root1:
            return
        if not root1.left and not root1.right:
            self.first.append(root1.val)
        else:
            self.check1(root1.left)
            self.check1(root1.right)

    def check2(self, root2):
        if not root2:
            return
        if not root2.left and not root2.right:
            self.second.append(root2.val)
        else:
            self.check2(root2.left)
            self.check2(root2.right)

    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not root1 or not root2:
            return False
        self.check1(root1)
        self.check2(root2)
        return self.first == self.second


# Runtime: 28 ms, faster than 83.59% of Python3 online submissions
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions
