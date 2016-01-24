from binaryTree import BinaryTree

tree = BinaryTree(1)
tree.insert_left(2)
tree.insert_right(3)
tree.get_left_child().insert_left(4)
tree.get_left_child().insert_right(5)
tree.get_right_child().insert_left(6)
tree.get_right_child().insert_right(7)
tree.left.left.insert_left(8)
tree.left.left.insert_right(9)
tree.right.left.insert_left(10)
tree.right.left.insert_right(11)
tree.right.right.insert_right(12)

p=[]
def leftmost(root):
	global p
	if root.left:
		p.append(root.key)
		leftmost(root.left)

def leaf(root):
	global p
	if not (root.right or root.left):
		p.append(root.key)
	if root.left:
		leaf(root.left)
	if root.right:
		leaf(root.right)

def rightmost(root):
	global p
	if root.right:
		rightmost(root.right)
		p.append(root.key)
	return p

def perimeter(root):
	q=[]
	if root==None:
		return
	else:
		leftmost(root)
		leaf(root)	
		q=rightmost(root)
		return q[:len(q)-1]

print perimeter(tree)