from binaryTree import BinaryTree
# MORRIS TRAVERSAL - INORDER TRAVERSAL IN O(1) SPACE
def morrisTraversal(root):
	while root!=None:
		if root.left != None:
			temp = root.left
			while temp.right!=None and temp.right!=root:
				temp = temp.right

			if temp.right == None:
				temp.right = root
				root = root.left
			else:
				temp.right = None
				print root.key
				root = root.right

		else:
			print root.key
			root = root.right



tree = BinaryTree(2)
tree.insert_left(1)
tree.insert_right(3)

morrisTraversal(tree)
