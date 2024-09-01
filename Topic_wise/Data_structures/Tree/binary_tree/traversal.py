"""
In-order, Pre-order, and Post-order Traversals are methods of visiting all the nodes in a tree,
specifically in a binary tree. Each method of traversal differs in the order in which nodes are visited.
These traversal methods are essential for various tree operations,
such as printing, searching, or modifying tree data.

1. In-order Traversal (Left, Root, Right)
In-order traversal visits the nodes of a binary tree in the following order:

Left Subtree: Visit all the nodes in the left subtree.
Root: Visit the root node.
Right Subtree: Visit all the nodes in the right subtree.

Use Case: In a Binary Search Tree (BST), performing an in-order traversal will visit the nodes in ascending order.

Example: For the following tree:
    10
   /  \
  5    20
 / \   / \
3   7 15  30

In-order Traversal: 3, 5, 7, 10, 15, 20, 30
"""

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

# In-order Traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)

"""
2. Pre-order Traversal (Root, Left, Right)
Pre-order traversal visits the nodes of a binary tree in the following order:

Root: Visit the root node first.
Left Subtree: Visit all the nodes in the left subtree.
Right Subtree: Visit all the nodes in the right subtree.

Use Case: Pre-order traversal is useful for creating a copy of the tree or for prefix notation of expressions.

Example: For the same tree:
    10
   /  \
  5    20
 / \   / \
3   7 15  30

Pre-order Traversal: 10, 5, 3, 7, 20, 15, 30
"""

# Pre-order Traversal
def preorder(root):
    if root:
        print(root.value, end=" ")
        preorder(root.left)
        preorder(root.right)

"""
3. Post-order Traversal (Left, Right, Root)
Post-order traversal visits the nodes of a binary tree in the following order:

Left Subtree: Visit all the nodes in the left subtree.
Right Subtree: Visit all the nodes in the right subtree.
Root: Visit the root node last.

Use Case: Post-order traversal is useful for deleting or freeing nodes, 
as it processes child nodes before the parent node.

Example: For the same tree:
    10
   /  \
  5    20
 / \   / \
3   7 15  30

Post-order Traversal: 3, 7, 5, 15, 30, 20, 10

"""

# Post-order Traversal
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value, end=" ")


# Driver code
if __name__ == "__main__":
    root = Node(10)
    root.left = Node(5)
    root.right = Node(20)
    root.left.left = Node(3)
    root.left.right = Node(7)
    root.right.left = Node(15)
    root.right.right = Node(30)

    print("In-order Traversal:")
    inorder(root)
    print("\nPre-order Traversal:")
    preorder(root)
    print("\nPost-order Traversal:")
    postorder(root)

"""
Output : 

In-order Traversal:
3 5 7 10 15 20 30 

Pre-order Traversal:
10 5 3 7 20 15 30 

Post-order Traversal:
3 7 5 15 30 20 10 

"""