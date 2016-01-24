from binaryTree import BinaryTree

tree=BinaryTree(1)
tree.insert_left(1)
tree.insert_right('A')
tree.left.insert_left('B')
tree.left.insert_right('C')

def leaf(node):
	if not (node.right or node.left):
		return True

def huffman(root,code):
	temp=root
	if temp==None:
		return
	for i in code:
		if i=='1':
			if temp.right:
				temp=temp.right
				if leaf(temp):
					print temp.key
					temp=root
				else:
					continue

		elif i=='0':
			if temp.left:
				temp=temp.left
				if leaf(temp):
					print temp.key
					temp=root
				else:
					continue


huffman(tree,"1001011")