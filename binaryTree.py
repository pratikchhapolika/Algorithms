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

tree = BinaryTree(1)
tree.insert_left(2)
tree.insert_right(3)
tree.left().insert_left(4)
tree.left().insert_right(5)
tree.right().insert_left(6)
tree.right().insert_right(7)
