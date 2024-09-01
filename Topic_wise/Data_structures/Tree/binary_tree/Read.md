# Binary Tree Implementation in Python

* A **binary tree** is a hierarchical data structure where each node has at most two children, 
commonly referred to as the left child and the right child. 
* Binary trees are widely used in various applications, such as searching, sorting, 
and data compression. Below is an overview of the binary tree structure, its properties, and its types.

## Properties
* **Node:** Each element in a binary tree is called a node. A node contains a value and pointers to its left and right children.
* **Root:** The top node of a binary tree is called the root. It is the starting point for traversing the tree.
* **Leaf:** A node with no children is called a leaf or terminal node.
* **Depth:** The depth of a node is the number of edges from the root to the node. The depth of the root is 0.
* **Height:** The height of a node is the number of edges from the node to the deepest leaf. The height of a leaf node is 0.
* **Level:** The level of a node is the number of edges from the root to that node, starting with level 0 for the root.
* **Subtree:** A subtree is a section of a binary tree consisting of a node and its descendants.


## Types of Binary Trees
- **Full Binary Tree:** A binary tree in which every node has either 0 or 2 children.

- **Complete Binary Tree:** A binary tree in which all levels are completely filled except possibly for the last level, which is filled from left to right.

- **Perfect Binary Tree:** A binary tree in which all internal nodes have exactly two children and all leaves are at the same level.

- **Balanced Binary Tree:** A binary tree in which the height of the left and right subtrees of every node differ by at most one.

- **Binary Search Tree (BST):** A binary tree in which for every node, all values in the left subtree are less than the node’s value, and all values in the right subtree are greater than the node’s value.

- **AVL Tree:** A self-balancing binary search tree where the difference between heights of left and right subtrees cannot be more than one.

- **Red-Black Tree:** A self-balancing binary search tree with an additional property: each node is either red or black, and the tree balances itself based on color properties.

- **Splay Tree:** A self-adjusting binary search tree with the additional property that recently accessed elements are quick to access again.

- **Treap:** A binary search tree that maintains heap properties based on randomly assigned priorities.