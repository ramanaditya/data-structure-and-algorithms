"""
[590. N-ary Tree Postorder Traversal](https://leetcode.com/problems/n-ary-tree-postorder-traversal/)
Given an n-ary tree, return the postorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

Recursive solution is trivial, could you do it iteratively?

Example 1:
Input: root = [1,null,3,2,4,null,5,6]
Output: [5,6,3,2,4,1]

Example 2:
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [2,6,14,11,7,3,12,8,4,13,9,10,5,1]
 

Constraints:
The height of the n-ary tree is less than or equal to 1000
The total number of nodes is between [0, 10^4]
"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def __init__(self):
        self.res = []
    def postorder(self, root: 'Node') -> List[int]:
        if root is not None:
            for i in root.children:
                self.postorder(i)
            self.res.append(root.val)
        return self.res


# Runtime: 52 ms, faster than 58.74% of Python3 online submissions
# Memory Usage: 14.9 MB, less than 100.00% of Python3 online submissions
