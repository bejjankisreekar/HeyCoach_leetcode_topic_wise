class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


# A function to insert a new node with the given key
def insert(root, key):
    # If the tree is empty, return a new node
    if root is None:
        return Node(key)

    # Otherwise, recur down the tree
    if key < root.value:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    # return the (unchanged) node pointer
    return root


# A function to do inorder tree traversal
def inorder(root):
    if root:
        # First recur on the left child
        inorder(root.left)
        # Then print the data of the node
        print(root.value, end=" ")
        # Finally recur on the right child
        inorder(root.right)


# Driver code
if __name__ == "__main__":
    root = None
    values = [20, 10, 30, 5, 15, 25, 35]

    # Construct the tree
    for value in values:
        root = insert(root, value)

    # Print inorder traversal of the tree
    print("Inorder Traversal of the tree:")
    inorder(root)
