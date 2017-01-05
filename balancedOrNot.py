from binaryTree import BinaryTree

tree = BinaryTree(1)
tree.insert_left(2)
tree.insert_right(3)
tree.left.insert_left(4)
tree.left.insert_right(5)
tree.left.left.insert_left(8)
tree.right.insert_left(6)

# def height(tree):
# 	if tree==None:
# 		return 0
# 	else:
# 		return max(height(tree.left), height(tree.right))+1

def balanced(tree):
	if tree==None:
		return True
	else:
		# h1=height(tree.left)
		# h2=height(tree.right)
		# if abs(h1-h2)<=1 and balanced(tree.left) and balanced(tree.right):
		# 	return 1
		# else:
		# 	return 0

		left_height = balanced(tree.left)
		if left_height==-1:
			return -1
		
		right_height = balanced(tree.right)
		if right_height==-1:
			return -1

		diff = abs(left_height - right_height)
		if diff>1:
			return -1
		else:
			return max(left_height, right_height) + 1

def check(tree):
	if balanced(tree)==-1:
		return False
	return True

print check(tree)
