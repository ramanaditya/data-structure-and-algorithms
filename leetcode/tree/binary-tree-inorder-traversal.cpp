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

//struct TreeNode {
//  int val;
//  TreeNode *left;
//  TreeNode *right;
//  TreeNode(int x) : val(x), left(NULL), right(NULL) {}
//};

class Solution {
public:
    vector<int> res;
    vector<int> inorderTraversal(TreeNode* root) {
        if(root != NULL){
            inorderTraversal(root->left);
            res.push_back(root->val);
            inorderTraversal(root->right);
        }
        return res;
    }
};


// Runtime: 0 ms, faster than 100.00% of C++ online submissions
// Memory Usage: 11.2 MB, less than 5.00% of C++ online submissions


class Solution {
// Iterative Method
public:
    vector<int> inorderTraversal(TreeNode* root) {
        if(root == NULL)
            return {};

        stack<TreeNode*> s;
        vector<int> res;

        while(root != NULL || !s.empty()) {
            while(root != NULL){
                s.push(root);
                root = root->left;
            }

            root = s.top();
            s.pop();
            res.push_back(root->val);

            root = root->right;
        }
        return res;
    }
};

// Runtime: 0 ms, faster than 100.00% of C++ online submissions
// Memory Usage: 8.6 MB, less than 25.83% of C++ online submissions
