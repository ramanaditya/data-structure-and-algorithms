/*
[104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
*/


/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

class Solution {
    public int maxDepth(TreeNode root) {
        int left, right;
        if(root == null){
            return 0;
        }else{
            left = maxDepth(root.left);
            right = maxDepth(root.right);
        }
        return (left > right ? left : right) + 1;
    }
}


// Runtime: 0 ms, faster than 100.00% of Java online submissions
// Memory Usage: 38.4 MB, less than 97.31% of Java online submissions
