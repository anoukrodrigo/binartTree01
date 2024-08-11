class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return Node(key)

        if key < root.value:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        return root

    def delete(self, root, key):
        if root is None:
            return root

        if key < root.value:
            root.left = self.delete(root.left, key)
        elif key > root.value:
            root.right = self.delete(root.right, key)
        else:
            # Node with only one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Node with two children, get the inorder successor
            temp = self.minValueNode(root.right)
            root.value = temp.value
            root.right = self.delete(root.right, temp.value)

        return root

    def minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorderTraversal(self, root):
        if root:
            self.inorderTraversal(root.left)
            print(root.value, end=' ')
            self.inorderTraversal(root.right)

    def preorderTraversal(self, root):
        if root:
            print(root.value, end=' ')
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)

    def postorderTraversal(self, root):
        if root:
            self.postorderTraversal(root.left)
            self.postorderTraversal(root.right)
            print(root.value, end=' ')


# Example usage:
tree = BinaryTree()
root = None

# Insert nodes
root = tree.insert(root, 50)
root = tree.insert(root, 30)
root = tree.insert(root, 20)
root = tree.insert(root, 40)
root = tree.insert(root, 70)
root = tree.insert(root, 60)
root = tree.insert(root, 80)

# Traversals
print("In-order traversal:")
tree.inorderTraversal(root)
print("\nPre-order traversal:")
tree.preorderTraversal(root)
print("\nPost-order traversal:")
tree.postorderTraversal(root)

# Delete node
root = tree.delete(root, 20)
print("\nIn-order traversal after deleting 20:")
tree.inorderTraversal(root)

root = tree.delete(root, 30)
print("\nIn-order traversal after deleting 30:")
tree.inorderTraversal(root)

root = tree.delete(root, 50)
print("\nIn-order traversal after deleting 50:")
tree.inorderTraversal(root)
