from binaryTree import BinaryTree

tree = BinaryTree(3)
tree.insert_left(5)
tree.insert_right(1)
tree.get_left_child().insert_left(6)
tree.get_left_child().insert_right(2)
tree.get_right_child().insert_left(9)
tree.get_right_child().insert_right(8)
#tree.get_left_child().get_left_child().insert_left(8)
tree.get_left_child().get_right_child().insert_left(7)
tree.get_left_child().get_right_child().insert_right(4)
# tree.get_right_child().get_left_child().insert_left(16)
# tree.get_right_child().get_right_child().insert_right(27)

def lca(root, value1, value2):
	if root==None:
		return

	if root.key==value1 or root.key==value2:
		return root.key

	left_lca = lca(root.left, value1, value2)
	right_lca = lca(root.right, value1, value2)

	# If the values are present in both
	# left subtree and right subtree
	if left_lca and right_lca:
		return root.key

	# If values are present only in left subtree
	if left_lca:
		return left_lca
	# If values are present only in right subtree
	else:
		return right_lca

print lca(tree, 2, 4)
