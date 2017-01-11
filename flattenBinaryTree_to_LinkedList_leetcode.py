def flatten(root):
	while root!=None:
		if root.left:
			temp = root.left
			while temp.right:
				temp = temp.right
			
			temp.right = root.right
			root.right = root.left
			root.left = None
		
		root = root.right

