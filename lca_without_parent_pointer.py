from binaryTree import BinaryTree

tree = BinaryTree(20)
tree.insert_left(8)
tree.insert_right(22)
tree.get_left_child().insert_left(4)
tree.get_left_child().insert_right(12)
tree.get_left_child().get_right_child().insert_left(10)
tree.get_left_child().get_right_child().insert_right(14)

def lca_without_parent(root, value1, value2): 
	while root!=None:
		if root.key > value1 and root.key > value2:
			root = root.left
		elif root.key < value1 and root.key < value2:
			root = root.right
		else:
			return root.key

print lca_without_parent(tree, 4, 14)