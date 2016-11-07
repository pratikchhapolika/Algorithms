from binaryTree import BinaryTree

tree = BinaryTree(26)
tree.insert_left(10)
tree.insert_right(3)
tree.get_left_child().insert_left(6)
tree.get_left_child().insert_right(4)
tree.get_right_child().insert_right(3)

def sum_nodes(root):
	if root==None:
		return 0
	return sum_nodes(root.left) + root.key + sum_nodes(root.right)

def sumtree(root):
	if root==None or (root.left==None and root.right==None):
		return 1
	ls = sum_nodes(root.left)
	rs = sum_nodes(root.right)

	if (root.key == ls+rs) and (sumtree(root.left)) and (sumtree(root.right)):
		return 1
	return 0


print sumtree(tree)
