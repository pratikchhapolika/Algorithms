from binaryTree import BinaryTree

tree = BinaryTree(1)
tree.insert_left(2)
tree.insert_right(3)
tree.left.insert_left(4)
tree.left.insert_right(5)
tree.left.left.insert_left(8)
tree.right.insert_left(6)

def height(tree):
	if tree==None:
		return 0
	else:
		return max(height(tree.left), height(tree.right))+1

l=[]
def balanced(tree):
	if tree==None:
		return 
	else:
		h1=height(tree.left)
		h2=height(tree.right)
		if abs(h1-h2)>1:
			l.append(False)
		else:
			l.append(True)
		if tree.left:
			balanced(tree.left)
		if tree.right:
			balanced(tree.right)

	return l

p=balanced(tree)
if False in p:
	print 'The binary tree is not height balanced'
else:
	print 'The binary tree is height balanced'