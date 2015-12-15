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

	def reverse(self):
		self.left, self.right=self.right, self.left
		print self.key
		if self.left:
			self.left.reverse()
		if self.right:
			self.right.reverse() 

tree = BinaryTree(5)
tree.insert_left(4)
tree.insert_right(5)
tree.get_left_child().insert_left(3)
tree.get_right_child().insert_right(7)

# tree.reverse()

# def preorder(tree):
# 	if tree!=None:
# 		print tree.get_root()
# 		preorder(tree.get_left_child())
# 		preorder(tree.get_right_child())

# def inorder(tree):
# 	if tree!=None:
# 		inorder(tree.get_left_child())
# 		print tree.get_root()
# 		inorder(tree.get_right_child())

# def postorder(tree):
# 	if tree!=None:
# 		postorder(tree.get_left_child())
# 		postorder(tree.get_right_child())
# 		print tree.get_root()


# inorder(tree)
# print
# preorder(tree)
# print
# postorder(tree)

l=[]
def check(tree):
	
	if tree!=None:
		if tree.get_left_child():
			if tree.get_left_child().get_root()<tree.get_root():
				l.append("bST")
				check(tree.get_left_child())
			else:
				l.append("not BST")

		if tree.get_right_child():
			if tree.get_right_child().get_root()>tree.get_root():
				l.append("BSt")
				check(tree.get_right_child())
			else:
				l.append("Not BSt")

	return l

print check(tree)

# def check(tree):
# 	if tree!=None:
# 		check(tree.get_left_child())
# 		l.append(tree.get_root())
# 		check(tree.get_right_child())
# 	if all(l[i] <= l[i+1] for i in xrange(len(l)-1)):
# 		return "BST"
# 	else:
# 		return "Not bst"

# print check(tree)



