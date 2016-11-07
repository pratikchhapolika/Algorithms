from binaryTree import BinaryTree

def inorder_traversal(root):
	if root!=None:
		inorder_traversal(root.left)
		print root.key,
		inorder_traversal(root.right)

def in_pre(inorder, preorder, start, end):
	if start>end:
		return None

	tree = BinaryTree(preorder[in_pre.index])
	in_pre.index+=1

	if start == end:
		return tree

	i = inorder.index(tree.key)

	tree.left = in_pre(inorder, preorder, start, i-1)
	tree.right = in_pre(inorder, preorder, i+1, end)

	return tree

inorder = ['D','B','E','A','F','C']
preorder = ['A','B','D','E','C','F']

in_pre.index = 0

root = in_pre(inorder, preorder, 0, len(preorder)-1)
inorder_traversal(root)
