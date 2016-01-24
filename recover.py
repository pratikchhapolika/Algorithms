from binaryTree import BinaryTree

tree=BinaryTree(1)
tree.insert_left(2)
tree.insert_right(3)

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

def recover(root):
	y=[]
	if root==None:
		return
	p=inorder(root)
	for i in range(len(p)-1):
		if p[i]>p[i+1]:
			y.extend([p[i],p[i+1]])

	return [min(y),max(y)]

print recover(tree)