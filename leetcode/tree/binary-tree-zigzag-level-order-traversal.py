"""
Medium
[103. Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/)
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values.
(i.e., from left to right, then right to left for the next level and alternate between).

Example 1:
    3
   / \
  9  20
    /  \
   15   7

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
"""

# Solutions

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_order_list = []

        def dfs(root, level):
            if not root:
                return

            # to avoid calculating the length each time, we can make level_order_list = [[], 0]
            # compare level with level_order_list[1], append into list at index 0,
            # and add 1 to the second index in each else statement
            # return the first(0) index of level_order_list, ie., level_order_list[0]
            if level < len(level_order_list):
                # Check for odd and even level here
                if level & 1:
                    level_order_list[level].appendleft(root.val)
                else:
                    level_order_list[level].append(root.val)
            else:
                level_order_list.append(deque([root.val]))

            dfs(root.left, level + 1)
            dfs(root.right, level + 1)

        dfs(root, 0)

        return level_order_list


# Runtime       : 65 ms, faster than 18.81% of Python3 online submissions
# Memory Usage  : 14.2 MB, less than 57.89% of Python3 online submissions
