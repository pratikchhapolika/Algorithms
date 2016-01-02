class BinaryTree(object):

	def __init__(self,root):
		self.key=root
		self.left=None
		self.right=None

	def insert_left(self,new_node):
		if self.left==None:
			self.left=BinaryTree(new_node)
		else:
			t=BinaryTree(new_node)
			t.left=self.left
			self.left=t

	def insert_right(self,new_node):
		if self.right==None:
			self.right=BinaryTree(new_node)
		else:
			t=BinaryTree(new_node)
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
 
tree = BinaryTree(3)
tree.insert_left(9)
tree.insert_right(20)
tree.get_left_child().insert_left(4)
tree.get_left_child().insert_right(5)
tree.get_right_child().insert_left(15)
tree.get_right_child().insert_right(7)
#tree.get_left_child().get_left_child().insert_left(8)
# tree.get_left_child().get_right_child().insert_left(11)
# tree.get_right_child().get_left_child().insert_left(16)
# tree.get_right_child().get_right_child().insert_right(27)

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







