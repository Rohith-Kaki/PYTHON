class TreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.height = 1  # Height of the node in the tree

class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return 0
        return node.height

    def balance(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def rotate_right(self, y):
        x = y.left
        T2 = x.right
        # Perform rotation
        x.right = y
        y.left = T2
        # Update heights
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))
        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left
        # Perform rotation
        y.left = x
        x.right = T2
        # Update heights
        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        return y

    def insert(self, root, key, value):
        # Perform standard BST insertion
        if root is None:
            return TreeNode(key, value)
        if key < root.key:
            root.left = self.insert(root.left, key, value)
        elif key > root.key:
            root.right = self.insert(root.right, key, value)
        else:
            return root  # Duplicate keys are not allowed
        # Update height of the current node
        root.height = 1 + max(self.height(root.left), self.height(root.right))
        # Perform balancing
        balance = self.balance(root)
        # Left Heavy
        if balance > 1:
            if key < root.left.key:
                return self.rotate_right(root)
            else:
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root)
        # Right Heavy
        if balance < -1:
            if key > root.right.key:
                return self.rotate_left(root)
            else:
                root.right = self.rotate_right(root.right)
                return self.rotate_left(root)
        return root

    def insert_category(self, key, value):
        self.root = self.insert(self.root, key, value)

    def search_category(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self.search_category(root.left, key)
        return self.search_category(root.right, key)

    def search(self, key):
        return self.search_category(self.root, key)

# Example usage:
if __name__ == "__main__":
    avl_tree = AVLTree()
    # Inserting categories
    avl_tree.insert_category("Electronics", "Category: Electronics")
    avl_tree.insert_category("Clothing", "Category: Clothing")
    avl_tree.insert_category("Books", "Category: Books")
    # Searching for categories
    search_result = avl_tree.search("Clothing")
    if search_result:
        print(f"Category found: {search_result.value}")
    else:
        print("Category not found.")
