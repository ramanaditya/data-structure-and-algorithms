/*
This file contains all the operations related to Binary Tree in Javas
*/
// Defining class for the Node
class Node {
    int key;
    Node left, right;

    // With every insertion of node left and right will be null initially
    public Node(int item){
        key = item;
        left = right = null;
    }
}

class BinaryTree{

    // Root of binary tree
    Node root;

    // Constructor for initializing root to null
    BinaryTree(){
        root = null;
    }

    public static void main(String[] args){
        BinaryTree tree = BinaryTree();

    }
}
