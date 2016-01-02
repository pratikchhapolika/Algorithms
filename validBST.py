from binaryTree import BinaryTree

tree = BinaryTree(5)
tree.insert_left(4)
tree.insert_right(5)
tree.get_left_child().insert_left(3)
tree.get_right_child().insert_right(7)


l=[]
# def check(tree):
	
# 	if tree!=None:
# 		if tree.get_left_child():
# 			if tree.get_left_child().get_root()<tree.get_root():
# 				l.append("bST")
# 				check(tree.get_left_child())
# 			else:
# 				l.append("not BST")

# 		if tree.get_right_child():
# 			if tree.get_right_child().get_root()>tree.get_root():
# 				l.append("BSt")
# 				check(tree.get_right_child())
# 			else:
# 				l.append("Not BSt")

# 	return l

# print check(tree)

def check(tree):
	if tree!=None:
		check(tree.get_left_child())
		l.append(tree.get_root())
		check(tree.get_right_child())
	if all(l[i] <= l[i+1] for i in xrange(len(l)-1)):
		return "BST"
	else:
		return "Not bst"

print check(tree)