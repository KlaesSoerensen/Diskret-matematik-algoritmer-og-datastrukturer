class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def count_red_black_trees(root):
    count_dict = {}
    return count_red_black_trees_helper(root, count_dict, False)


def count_red_black_trees_helper(node, count_dict, parent_red):
    if node is None:
        return 1

    if (node, parent_red) in count_dict:
        return count_dict[(node, parent_red)]

    total_count = 0

    # Recursively count the number of valid red-black trees for the left and right subtrees
    for left_color in [False, True]:
        for right_color in [False, True]:
            if (parent_red or not left_color) and (parent_red or not right_color):
                left_count = count_red_black_trees_helper(node.left, count_dict, left_color)
                right_count = count_red_black_trees_helper(node.right, count_dict, right_color)
                total_count += left_count * right_count

    count_dict[(node, parent_red)] = total_count

    # Check the height balance condition for the current node
    if is_height_balanced(node):
        return total_count
    else:
        return 0


def is_height_balanced(node):
    if node is None:
        return True

    left_height = get_height(node.left)
    right_height = get_height(node.right)

    return abs(left_height - right_height) <= 1 and is_height_balanced(node.left) and is_height_balanced(node.right)


def get_height(node):
    if node is None:
        return 0

    return 1 + max(get_height(node.left), get_height(node.right))


# Example usage
# Create the binary tree
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.left = TreeNode(13)
root.right.left.right = TreeNode(14)
root.right.right = TreeNode(17)
root.right.right.right = TreeNode(16)
root.right.right.right.right = TreeNode(18)

""" root.right.left.right = TreeNode(14)
root.right.right = TreeNode(17)
root.right.right.right = TreeNode(16)
root.right.right.right.right = TreeNode(18) """

# Count the number of valid red-black trees
valid_count = count_red_black_trees(root)
print("Number of valid red-black trees:", valid_count)
