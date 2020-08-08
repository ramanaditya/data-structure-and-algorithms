"""
[987. Vertical Order Traversal of a Binary Tree](https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/)
Given a binary tree, return the vertical order traversal of its nodes values.

For each node at position (X, Y), its left and right children respectively will be at positions (X-1, Y-1) and (X+1, Y-1).

Running a vertical line from X = -infinity to X = +infinity, whenever the vertical line touches some nodes, we report
the values of the nodes in order from top to bottom (decreasing Y coordinates).

If two nodes have the same position, then the value of the node that is reported first is the value that is smaller.

Return an list of non-empty reports in order of X coordinate.  Every report will have a list of values of nodes.

Example 1:
Input: [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation:
Without loss of generality, we can assume the root node is at position (0, 0):
Then, the node with value 9 occurs at position (-1, -1);
The nodes with values 3 and 15 occur at positions (0, 0) and (0, -2);
The node with value 20 occurs at position (1, -1);
The node with value 7 occurs at position (2, -2).

Example 2:
Input: [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation:
The node with value 5 and the node with value 6 have the same position according to the given scheme.
However, in the report "[1,5,6]", the node value of 5 comes first since 5 is smaller than 6.


Note:
The tree will have between 1 and 1000 nodes.
Each node's value will be between 0 and 1000.
"""


# Solutions

# Definition for a binary tree node.
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Time Complexity: O( n log n ), as sorted at each level of the tree + recusrsion
    Space Complexity: O( n )
    """

    def __init__(self):
        # Constants for the iteration
        self.max_level = float("-inf")
        self.min_level = float("inf")

    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        res_dict = defaultdict(list)

        # x is for depth and y is for the width
        def dfs(root, x, y):
            # Base Case
            if not root:
                return

            # Setting min and max value for the iteration
            self.min_level = min(x, self.min_level)
            self.max_level = max(x, self.max_level)

            # Forming dictionary with keys as x-level
            res_dict[x].append((y, root.val))

            # Recursion
            dfs(root.left, x - 1, y + 1)
            dfs(root.right, x + 1, y + 1)

        dfs(root, 0, 0)

        res = []

        # Iterating over each level
        for ind in range(self.min_level, self.max_level + 1):
            # Appending with list by sorting wrt to their y-level
            # For the condition to add the value based on their order of occurrence
            res.append([v for k, v in sorted(res_dict[ind])])

        return res


# Runtime: 28 ms, faster than 96.01% of Python3 online submissions
# Memory Usage: 14 MB, less than 57.15% of Python3 online submissions
