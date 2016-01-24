from binaryTree import BinaryTree

tree = BinaryTree(5)
tree.insert_left(4)
tree.insert_right(8)
tree.get_left_child().insert_left(11)
# tree.get_left_child().insert_right(2)
tree.get_right_child().insert_left(13)
tree.get_right_child().insert_right(4)
tree.get_left_child().get_left_child().insert_left(7)
tree.left.left.insert_right(2)
tree.right.right.insert_right(1)
tree.right.right.insert_left(5)

# def path(tree):
# 	paths = []
# 	if not (tree.left or tree.right):
# 		return [[tree.key]]    # this will return all the leaf nodes
# 	if tree.left:
# 		paths.extend([[tree.key] + child for child in path(tree.left)])
# 	if tree.right:
# 		paths.extend([[tree.key] + child for child in path(tree.right)])
# 	return paths

# k=22
# p=[]
# p=path(tree)
# print p
# for i in p:
# 	if sum(i)==k:
# 		print 1

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

	for k,val in d.items():
		if k==node:
			return val

p=[]
def leaf(tree):
	if not (tree.left or tree.right):
		p.append(tree)
	if tree.left:
		leaf(tree.left)
	if tree.right:
		leaf(tree.right)
	return p


def path(tree):
	l=[]
	ans=[]
	final=[]
	l=leaf(tree)
	for i in l:
		ans=[]
		d=depth(tree,i)
		while d>-1:
			ans.append(i.key)
			i=tree.node_parent(i)
			d-=1
		final.append(ans)
	
	for index,i in enumerate(final):
		i=i[::-1]
		final[index]=i

	return final

# print path(tree)

def sumrootleaf():
	list_tree=[]
	list_tree=path(tree)
	y=[]
	for i in list_tree:
		y.append(map(str,i))
	sum_tree=0
	for i in y:
		sum_tree+=int(''.join(i))
	print sum_tree
sumrootleaf()

