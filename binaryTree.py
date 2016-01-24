class BinaryTree(object):

	def __init__(self,root,parent=None):
		self.key=root
		self.left=None
		self.right=None
		self.parent=parent

	def insert_left(self,new_node,parent=None):
		if self.left==None:
			self.left=BinaryTree(new_node,parent=self)  # returns the parent
		else:
			t=BinaryTree(new_node,parent=self)
			t.left=self.left
			self.left=t

	def insert_right(self,new_node,parent=None):
		if self.right==None:
			self.right=BinaryTree(new_node,parent=self)
		else:
			t=BinaryTree(new_node,parent=self)
			t.right=self.right
			self.right=t

	def get_right_child(self):
		return self.right

	def get_left_child(self):
		return self.left

	def set_root(self,obj):
		self.key=obj

	def get_root(self):
		return self.key

	def node_parent(self,node):
		return node.parent


 
# tree = BinaryTree(1)
# tree.insert_left(2)
# tree.insert_right(3)
# tree.get_left_child().insert_left(4)
# tree.get_left_child().insert_right(5)
# tree.get_right_child().insert_left(6)
# tree.get_right_child().insert_right(7)
# tree.left.left.insert_left(8)
# tree.left.left.insert_right(9)
# tree.right.left.insert_left(10)
# tree.right.left.insert_right(11)
# tree.right.right.insert_right(12)


# def reverse(tree):
# 	if tree!=None:
# 		tree.left,tree.right=tree.right,tree.left
# 		if tree.left:
# 			reverse(tree.left)
# 		if tree.right:
# 			reverse(tree.right)
# reverse(tree)


# def preorder(tree):
# 	if tree!=None:
# 		print tree.key
# 		preorder(tree.left)
# 		preorder(tree.right)


# def inorder(tree):
# 	if tree!=None:
# 		inorder(tree.left)
# 		print tree.key
# 		inorder(tree.right)

# def postorder(tree):
# 	if tree!=None:
# 		postorder(tree.left)
# 		postorder(tree.right)
# 		print tree.key


# inorder(tree)
# print
# preorder(tree)
# print
# postorder(tree)

# l=[]
# def inorder(tree):
# 	global l
# 	if tree==None:
# 		return
# 	else:
# 		inorder(tree.left)
# 		l.append(tree.key)
# 		inorder(tree.right)
# 	return l

# print inorder(tree)

# def getSuccessor(tree, B):
# 	suc=[]
# 	if tree==None:
# 		return
# 	else:
# 		suc=inorder(tree)
# 		ind=suc.index(B)
# 		return suc[ind+1]

# print getSuccessor(tree,10)



# def height(tree):
# 	if tree==None:
# 		return 0
# 	else:
# 		return max(height(tree.left), height(tree.right))+1

# print height(tree)

# def kthsmallest(root, k):
# 	p=[]
# 	p=inorder(root)
# 	return p[k-1]

# print kthsmallest(tree,3)


# from unorderedLinkedList import UnorderedList
# u=UnorderedList()
# def preorder(tree):
# 	if tree==None:
# 		return
# 	else:
# 		u.add(tree.key)
# 		preorder(tree.left)
# 		preorder(tree.right)
# 		return u

# l=preorder(tree)
# l.reverse()
# l.display()

