from queue import Queue
from binaryTree import BinaryTree

q=Queue()
def levelorder(root):
	if root==None:
		return 0
	else:
		# USING RECURSION
		# print root.key
		# if root.left:
		# 	q.enqueue(root.left)
		# if root.right:
		# 	q.enqueue(root.right)
		# if q.size()>0:
		# 	return levelorder(q.dequeue())

		# USING ITERATION
		q.enqueue(root)
		l=[]
		while q.size()>0:
			current=q.dequeue()
			l.append(current.key)

			if current.left:
				q.enqueue(current.left)
			if current.right:
				q.enqueue(current.right)
		return l

tree = BinaryTree(3)
tree.insert_left(9)
tree.insert_right(20)
tree.get_left_child().insert_left(4)
tree.get_left_child().insert_right(5)
tree.get_right_child().insert_left(15)
tree.get_right_child().insert_right(7)

print levelorder(tree)