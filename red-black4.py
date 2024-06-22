class Node:
    def __init__(self, key, color='RED'):
        self.key = key
        self.color = color
        self.left = None
        self.right = None
        self.parent = None


class RedBlackTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        node = Node(key)
        if self.root is None:
            node.color = 'BLACK'
            self.root = node
        else:
            self._insert_recursive(self.root, node)
            self._fix_insertion(node)

    def _insert_recursive(self, root, node):
        if root is None:
            return node

        if node.key < root.key:
            root.left = self._insert_recursive(root.left, node)
            root.left.parent = root
        else:
            root.right = self._insert_recursive(root.right, node)
            root.right.parent = root

        return root

    def _fix_insertion(self, node):
        while node.parent is not None and node.parent.color == 'RED':
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right

                if uncle is not None and uncle.color == 'RED':
                    node.parent.color = 'BLACK'
                    uncle.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self._rotate_left(node)

                    node.parent.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    self._rotate_right(node.parent.parent)
            else:
                uncle = node.parent.parent.left

                if uncle is not None and uncle.color == 'RED':
                    node.parent.color = 'BLACK'
                    uncle.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._rotate_right(node)

                    node.parent.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    self._rotate_left(node.parent.parent)

        self.root.color = 'BLACK'

    def _rotate_left(self, node):
        right_child = node.right
        node.right = right_child.left

        if right_child.left is not None:
            right_child.left.parent = node

        right_child.parent = node.parent

        if node.parent is None:
            self.root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child

        right_child.left = node
        node.parent = right_child

    def _rotate_right(self, node):
        left_child = node.left
        node.left = left_child.right

        if left_child.right is not None:
            left_child.right.parent = node

        left_child.parent = node.parent

        if node.parent is None:
            self.root = left_child
        elif node == node.parent.left:
            node.parent.left = left_child
        else:
            node.parent.right = left_child

        left_child.right = node
        node.parent = left_child

    def delete(self, key):
        node = self.search(key)
        if node is None:
            return

        self._delete_node(node)

    def _delete_node(self, node):
        if node.left is not None and node.right is not None:
            successor = self._minimum(node.right)
            node.key = successor.key
            node = successor

        child = node.left if node.left is not None else node.right

        if child is not None:
            child.parent = node.parent

        if node.parent is None:
            self.root = child
        else:
            if node == node.parent.left:
                node.parent.left = child
            else:
                node.parent.right = child

        if node.color == 'BLACK':
            self._fix_deletion(child, node.parent)

    def _fix_deletion(self, node, parent):
        while node != self.root and (node is None or node.color == 'BLACK'):
            if node == parent.left:
                sibling = parent.right

                if sibling.color == 'RED':
                    sibling.color = 'BLACK'
                    parent.color = 'RED'
                    self._rotate_left(parent)
                    sibling = parent.right

                if (sibling.left is None or sibling.left.color == 'BLACK') and \
                        (sibling.right is None or sibling.right.color == 'BLACK'):
                    sibling.color = 'RED'
                    node = parent
                    parent = node.parent
                else:
                    if sibling.right is None or sibling.right.color == 'BLACK':
                        sibling.left.color = 'BLACK'
                        sibling.color = 'RED'
                        self._rotate_right(sibling)
                        sibling = parent.right

                    sibling.color = parent.color
                    parent.color = 'BLACK'
                    sibling.right.color = 'BLACK'
                    self._rotate_left(parent)
                    node = self.root
            else:
                sibling = parent.left

                if sibling.color == 'RED':
                    sibling.color = 'BLACK'
                    parent.color = 'RED'
                    self._rotate_right(parent)
                    sibling = parent.left

                if (sibling.right is None or sibling.right.color == 'BLACK') and \
                        (sibling.left is None or sibling.left.color == 'BLACK'):
                    sibling.color = 'RED'
                    node = parent
                    parent = node.parent
                else:
                    if sibling.left is None or sibling.left.color == 'BLACK':
                        sibling.right.color = 'BLACK'
                        sibling.color = 'RED'
                        self._rotate_left(sibling)
                        sibling = parent.left

                    sibling.color = parent.color
                    parent.color = 'BLACK'
                    sibling.left.color = 'BLACK'
                    self._rotate_right(parent)
                    node = self.root

        if node is not None:
            node.color = 'BLACK'

    def _minimum(self, node):
        while node.left is not None:
            node = node.left
        return node

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None or node.key == key:
            return node

        if key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)

    def print_tree(self):
        if self.root is not None:
            self._print_tree_recursive(self.root, "", True)

    def _print_tree_recursive(self, node, indent, is_last):
        if node is not None:
            print(indent, end="")
            if is_last:
                print("└── ", end="")
                indent += "    "
            else:
                print("├── ", end="")
                indent += "|   "

            print(f"Key: {node.key}, Color: {node.color}")

            self._print_tree_recursive(node.left, indent, False)
            self._print_tree_recursive(node.right, indent, True)

import sys
def main():
    tree = RedBlackTree()
    cliInputRecieved = False

    # Expected CLI syntax array="1 2 3 4 5 6"
    for arg in sys.argv:
        if arg.startswith("array="):
            cliInputRecieved = True
            splitOnEquals = arg.split("=")[1]
            splitOnSpace = splitOnEquals.strip().split(" ")
            for num in splitOnSpace:
                tree.insert(int(num))

    if not cliInputRecieved:
        for num in [23, 7, 2, 27, 20, 5, 26, 18, 24, 21]:
            tree.insert(num)

    tree.print_tree()
    
    #print("Deleting node with key 10")
    #tree.delete(6)
    
    tree.print_tree()

if __name__ == '__main__':
    main()
