from binaryTree import BinaryTree

tree = BinaryTree(5)
tree.insert_left(4)
tree.insert_right(8)
tree.get_left_child().insert_left(11)
# tree.get_left_child().insert_right(2)
tree.get_right_child().insert_left(13)
tree.get_right_child().insert_right(4)
tree.get_left_child().get_left_child().insert_left(7)
tree.left.left.insert_right(2)
tree.right.right.insert_right(1)
tree.right.right.insert_left(5)

# def path(tree):
# 	paths = []
# 	if tree.left==None and tree.right==None:
# 		return [[tree.key]]    # this will return all the leaf nodes
# 	if tree.left:
# 		paths.extend([tree.key] + child for child in path(tree.left))
# 	if tree.right:
# 		paths.extend([tree.key] + child for child in path(tree.right))
# 	return paths

# print path(tree)



# O(n) solution
def path(tree, nodes=[]):
	if tree==None:
		return
	
	if tree.left==None and tree.right==None:
		nodes = nodes + [tree.key]
		print nodes 
	else:
		path(tree.left, nodes+[tree.key])
		path(tree.right, nodes+[tree.key])
path(tree)

