/*
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
*/

// Solutions

// Recursive Solution



// Definition for a binary tree node.
// public class TreeNode {
//   int val;
//   TreeNode left;
//   TreeNode right;
//   TreeNode(int x) { val = x; }
// }


class Solution {
    List<Integer> res = new ArrayList();
    public List<Integer> inorderTraversal(TreeNode root) {
        if(root != null){
            inorderTraversal(root.left);
            res.add(root.val);
            inorderTraversal(root.right);
        }
        return res;
    }
}


// Runtime: 0 ms, faster than 100.00% of Java online submissions
// Memory Usage: 37.9 MB, less than 5.11% of Java online submissions
