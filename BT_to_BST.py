from binaryTree import BinaryTree

tree = BinaryTree(10)
tree.insert_left(2)
tree.insert_right(7)
tree.get_left_child().insert_left(8)
tree.get_left_child().insert_right(4)

def preorder(root):
	if root!=None:
		print root.key,
		preorder(root.left)
		preorder(root.right)

def inorder(root, l):
	if root!=None:
		inorder(root.left, l)
		l.append(root.key)
		inorder(root.right, l)

def replace_inorder(root, l):
	if root!=None:
		replace_inorder(root.left, l)
		root.key = l.pop()
		replace_inorder(root.right, l)

def convert(root):
	l=[]
	inorder(root, l)
	l = sorted(l)
	replace_inorder(root, l[::-1])
	preorder(root)

convert(tree)
