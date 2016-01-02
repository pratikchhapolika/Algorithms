from binaryTree import BinaryTree

def zigzag(root):
	if root==None:
		return 0
	else:
		queue=[root]
		ans=[]
		line=0
		while queue:
			level=[]
			size=len(queue)
			for i in range(size):
				node=queue.pop(0)
				if node:
					if line%2==0:
						level.append(node.key)
					else:
						level.insert(0,node.key)
				
				if node.left:
					queue.append(node.left)
				if node.right:
					queue.append(node.right)

			ans.append(level)
			line+=1
		return ans

tree = BinaryTree(3)
tree.insert_left(9)
tree.insert_right(20)
tree.get_left_child().insert_left(4)
tree.get_left_child().insert_right(5)
tree.get_right_child().insert_left(15)
tree.get_right_child().insert_right(7)

print zigzag(tree)