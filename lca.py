from binaryTree import BinaryTree

tree = BinaryTree(3)
tree.insert_left(5)
tree.insert_right(1)
tree.get_left_child().insert_left(6)
tree.get_left_child().insert_right(2)
tree.get_right_child().insert_left(0)
tree.get_right_child().insert_right(8)
#tree.get_left_child().get_left_child().insert_left(8)
tree.get_left_child().get_right_child().insert_left(7)
tree.get_left_child().get_right_child().insert_right(4)
# tree.get_right_child().get_left_child().insert_left(16)
# tree.get_right_child().get_right_child().insert_right(27)

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

def depth(root,node):
	count=0
	if root==None:
		return 0
	q=[root]
	level=0
	d={}
	while q:
		size=len(q)
		for i in range(size):
			current=q.pop()
			d[current]=level
			if current.left:
				q.insert(0,current.left)
			if current.right:
				q.insert(0,current.right)
			
		level+=1

	for key,val in d.items():
		if key==node:
			return val
	

def lca(root,v,w):
	p=[]
	if root==None:
		return -1
	p=inorder(root)
	if v.key not in p or w.key not in p:
		return -1

	dv=depth(root,v)
	dw=depth(root,w)

	while dv>dw:
		v=root.node_parent(v)
		dv-=1

	while dv<dw:
		w=root.node_parent(w)
		dw-=1

	while v!=w:
		v=root.node_parent(v)
		w=root.node_parent(w)

	return v.key


print lca(tree,tree.left,tree.right.left)