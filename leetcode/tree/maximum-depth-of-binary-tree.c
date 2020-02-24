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
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */


int maxDepth(struct TreeNode* root){
    int left,right;
    if(root==NULL){
        return 0;
    }else{
        left = maxDepth(root->left);
        right = maxDepth(root->right);
    }
    if(left > right){
        return left+1;
    }
    return right+1;
}



// Runtime: 4 ms, faster than 95.45% of C online submissions
// Memory Usage: 9.3 MB, less than 66.67% of C online submissions
