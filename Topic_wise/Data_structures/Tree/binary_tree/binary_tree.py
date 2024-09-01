class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Inserts a value into the binary tree."""
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, current_node):
        """Helper function to insert a value in the correct position."""
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert(value, current_node.left)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert(value, current_node.right)

    def search(self, value):
        """Searches for a value in the binary tree."""
        return self._search(value, self.root)

    def _search(self, value, current_node):
        """Helper function to search for a value."""
        if current_node is None:
            return False
        elif value == current_node.value:
            return True
        elif value < current_node.value:
            return self._search(value, current_node.left)
        else:
            return self._search(value, current_node.right)

    def in_order_traversal(self):
        """Returns the in-order traversal of the binary tree."""
        result = []
        self._in_order_traversal(self.root, result)
        return result

    def _in_order_traversal(self, node, result):
        """Helper function for in-order traversal."""
        if node:
            self._in_order_traversal(node.left, result)
            result.append(node.value)
            self._in_order_traversal(node.right, result)

    def delete(self, value):
        """Deletes a value from the binary tree."""
        self.root = self._delete(self.root, value)

    def _delete(self, node, value):
        """Helper function to delete a node."""
        if node is None:
            return node

        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            # Node with only one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Node with two children: Get the inorder successor (smallest in the right subtree)
            min_larger_node = self._get_min(node.right)
            node.value = min_larger_node.value
            node.right = self._delete(node.right, min_larger_node.value)

        return node

    def _get_min(self, node):
        """Helper function to find the minimum value node in a subtree."""
        current = node
        while current.left is not None:
            current = current.left
        return current

# Example Usage
if __name__ == "__main__":
    bt = BinaryTree()
    bt.insert(10)
    bt.insert(5)
    bt.insert(20)
    bt.insert(3)
    bt.insert(7)
    bt.insert(15)
    bt.insert(30)

    print("In-Order Traversal:", bt.in_order_traversal())  # Output: [3, 5, 7, 10, 15, 20, 30]
    print("Search 15:", bt.search(15))  # Output: True
    print("Search 100:", bt.search(100))  # Output: False

    bt.delete(20)
    print("In-Order Traversal after deleting 20:", bt.in_order_traversal())  # Output: [3, 5, 7, 10, 15, 30]
