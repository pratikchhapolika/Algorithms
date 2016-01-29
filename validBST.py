from binaryTree import BinaryTree

tree = BinaryTree(5)
tree.insert_left(4)
tree.insert_right(5)
# tree.get_left_child().insert_left(3)
# tree.get_right_child().insert_right(7)


l=[]
def check(tree):
	if tree!=None:
		if tree.left:
			if tree.left.key<tree.key:
				l.append("bST")
				check(tree.left)
			else:
				l.append("not BST")

		if tree.right:
			if tree.right.key>tree.key:
				l.append("BSt")
				check(tree.right)
			else:
				l.append("Not BSt")

	return l

print check(tree)

# def check(tree):
# 	if tree!=None:
# 		check(tree.get_left_child())
# 		l.append(tree.get_root())
# 		check(tree.get_right_child())
# 	if all(l[i] <= l[i+1] for i in xrange(len(l)-1)):
# 		return "BST"
# 	else:
# 		return "Not bst"

# print check(tree)