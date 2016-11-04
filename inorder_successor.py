# This code executes in O(1) space. You can always use inorder traversal
# if space restriction in not given

from binaryTree import BinaryTree

tree=BinaryTree(20)
tree.insert_left(8)
tree.insert_right(22)
tree.left.insert_left(4)
tree.left.insert_right(12)
tree.left.right.insert_left(10)
tree.left.right.insert_right(14)

temp=tree.left.right.right

def findMinimum(root):
	while root.left!=None:
		root=root.left
	return root

def inorderSuccessor(root,temp):
	if root==None:
		return 
	elif temp.right!=None:
		y=findMinimum(temp.right)
		return y.key
	else:
		p=temp.parent
		while p!=None and p.right==temp:
			temp=p
			p=p.parent
		return p.key

print inorderSuccessor(tree,temp)