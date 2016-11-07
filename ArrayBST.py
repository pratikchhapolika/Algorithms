from binaryTree import BinaryTree

def arrayBST(l,start,end):
	mid=(start+end)/2
	if start<=end:
		tree=BinaryTree(l[mid])
		tree.left=arrayBST(l,start,mid-1)
		tree.right=arrayBST(l,mid+1,end)
		return tree

def inorder(tree):
	if tree!=None:
		inorder(tree.left)
		print tree.key,
		inorder(tree.right)

def preorder(tree):
	if tree!=None:
		print tree.key,
		preorder(tree.left)
		preorder(tree.right)

t=arrayBST([1,2,3,4],0,3)

inorder(t)
print 
preorder(t)