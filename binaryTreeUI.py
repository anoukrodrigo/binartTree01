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
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

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


def main():
    tree = BinaryTree()
    root = None

    while True:
        print("\nOptions:")
        print("1. Insert a node")
        print("2. Delete a node")
        print("3. In-order traversal")
        print("4. Pre-order traversal")
        print("5. Post-order traversal")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            key = int(input("Enter the value to insert: "))
            root = tree.insert(root, key)
        elif choice == 2:
            key = int(input("Enter the value to delete: "))
            root = tree.delete(root, key)
        elif choice == 3:
            print("In-order traversal:")
            tree.inorderTraversal(root)
            print()  # New line for better formatting
        elif choice == 4:
            print("Pre-order traversal:")
            tree.preorderTraversal(root)
            print()  # New line for better formatting
        elif choice == 5:
            print("Post-order traversal:")
            tree.postorderTraversal(root)
            print()  # New line for better formatting
        elif choice == 6:
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
