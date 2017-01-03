from binaryTree import BinaryTree

# tree = BinaryTree(5)
# tree.insert_left(4)
# tree.insert_right(8)
# tree.get_left_child().insert_left(11)
# # tree.get_left_child().insert_right(2)
# tree.get_right_child().insert_left(13)
# tree.get_right_child().insert_right(4)
# tree.get_left_child().get_left_child().insert_left(7)
# tree.left.left.insert_right(2)
# tree.right.right.insert_right(1)
# tree.right.right.insert_left(5)

tree = BinaryTree(2)
tree.insert_left(1)
tree.left.insert_left(4)
tree.insert_right(3)
tree.right.insert_right(5)

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
def path(tree, l, nodes=[]):
	if tree==None:
		return
	if tree.left==None and tree.right==None:
		nodes = nodes + [tree.key]
		l.append(nodes)
	else:
		path(tree.left, l, nodes+[tree.key])
		path(tree.right, l, nodes+[tree.key])

# def all_paths(tree):
# 	if tree==None:
# 		return
# 	path(tree)
# 	if tree.left:
# 		all_paths(tree.left)
# 	if tree.right:
# 		all_paths(tree.right)

l=[]
path(tree, l)

for i in l:
	print type(''.join(map(str, i)))

