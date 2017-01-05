from binaryTree import BinaryTree

def inorder_traversal(root):
	if root!=None:
		inorder_traversal(root.left)
		print root.key,
		inorder_traversal(root.right)

def in_post(inorder, postorder, start, end):
	if start>end:
		return None

	tree = BinaryTree(postorder[in_post.index])
	in_post.index-=1

	if start == end:
		return tree

	i = inorder.index(tree.key)

	tree.right = in_post(inorder, postorder, i+1, end)
	tree.left = in_post(inorder, postorder, start, i-1)

	return tree

inorder = [4, 8, 2, 5, 1, 6, 3, 7]
postorder = [8, 4, 5, 2, 6, 7, 3, 1]


in_post.index = len(postorder)-1

root = in_post(inorder, postorder, 0, len(postorder)-1)
inorder_traversal(root)
