"""
[257. Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths/)
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:
Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
"""


# Solutions

# Definition for a binary tree node.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def __init__(self):
        self.temp = []
        self.path = []

    def binaryTreePaths(self, root: TreeNode, level=0) -> List[str]:
        if root is None:
            return
        while len(self.temp) > level:
            self.temp.pop()
        self.temp.append(root.val)
        level += 1
        if not root.left and not root.right:
            string = "->".join([str(i) for i in self.temp])
            self.path.append(string)
        else:
            self.binaryTreePaths(root.left, level)
            self.binaryTreePaths(root.right, level)
        return self.path


# Runtime: 28 ms, faster than 82.09% of Python3 online submissions
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions
