from queue import Queue
from binaryTree import BinaryTree


def vertical(root):
	if root==None:
		return 0
	
	q = []
	q = [[root, 0]]

	d = {}

	while q:
		current, vertical_level = q.pop()
		
		if vertical_level in d:
			d[vertical_level].append(current.key)
		else:
			d[vertical_level] = [current.key]

		if current.left:
			q.append([current.left, vertical_level - 1])
		if current.right:
			q.append([current.right, vertical_level + 1])

	temp = sorted(d)

	for i in temp:
		print d[i]



tree = BinaryTree(1)
tree.insert_left(2)
tree.insert_right(3)
tree.get_left_child().insert_left(4)
tree.get_left_child().insert_right(5)
tree.get_right_child().insert_left(6)
tree.get_right_child().insert_right(7)
tree.get_left_child().get_left_child().insert_left(8)
tree.get_right_child().get_left_child().insert_right(9)

vertical(tree)