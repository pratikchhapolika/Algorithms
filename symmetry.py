from binaryTree import BinaryTree

l=[]
def inorder(tree):
	global l
	if tree==None:
		return
	else:
		inorder(tree.left)
		l.append(tree.key)
		inorder(tree.right)
	return l

def Symmetry():
	equal=True
	sym=inorder(tree)
	length=len(sym)
	print sym

	while length>1 and equal:
		first=sym.pop()
		last=sym.pop(0)
		length-=2
		if first==last:
			equal=True
			continue
		else:
			equal=False
	print equal

tree = BinaryTree(3)
tree.insert_left(9)
tree.insert_right(20)
tree.get_left_child().insert_left(4)
tree.get_left_child().insert_right(5)
tree.get_right_child().insert_left(15)
tree.get_right_child().insert_right(7)

Symmetry()