class BinarySearchTree(object):

	def __init__(self):
		self.root=None
		self.size=0

	def length(self):
		return self.size

	def __len__(self):
		return self.size

	def __iter__(self):
		return self.root.__iter__()

	def put(self,key,val):
		if self.root:
			self._put(key,val,self.root)
		else:
			self.root=TreeNode(key,val)

		self.size+=1

	def _put(self,key,val,currentnode):
		if key<currentnode.key:
			if currentnode.hasLeftChild():
				self._put(key,val,currentnode.leftChild)
			else:
				currentnode.leftChild=TreeNode(key,val,parent=currentnode)

		else:
			if currentnode.hasRightChild():
				self._put(key,val,currentnode.rightChild)
			else:
				currentnode.rightChild=TreeNode(key,val,parent=currentnode)

	def __setitem__(self,k,v):
		self.put(k,v)

	def get(self,key):
		if self.root:
			res=self._get(key,self.root)
			if res:
				return res.payload
			else:
				return None
		else:
			return None

	def _get(self,key,currentnode):
		if not currentnode:
			return None
		elif key==currentnode.key:
			return currentnode
		elif key<currentnode.key:
			self._get(key,currentnode.leftChild)
		else:
			self._get(key,currentnode.rightChild)

	def __getitem__(self,k):
		self.get(k)

	def __contains__(self,key):
		if self._get(key,self.root):
			return True
		else:
			return False

	def delete(self,key):
		if self.size>1:
			nodeToRemove=self._get(key,self.root)
			if nodeToRemove:
				self.remove(nodeToRemove)
				self.size-=1
			else:
				raise KeyError("Error, key not found")

		elif size==1 and self.root.key==key:
			self.root=None
			self.size-=1
		else:
			raise KeyError("Error, key not found")

	def __delitem__(self,k):
		self.delete(k)

	def remove(self,currentnode):
		if currentnode.isLeaf():
			if currentnode==currentnode.parent.leftChild:
				currentnode.parent.leftChild=None
			else:
				currentnode.parent.rightChild=None
		


class TreeNode(object):

	def __init__(self,key,val,left=None,right=None,parent=None):
		self.key=key
		self.payload=val
		self.leftChild=left
		self.rightChild=right
		self.parent=parent

	def hasLeftChild(self):
		return self.leftChild

	def hasRightChild(self):
		return self.rightChild

	def isLeftChild(self):
		return self.parent and self.parent.leftChild==self

	def isRightChild(self):
		return self.parent and self.parent.rightChild==self

	def isRoot(self):
		return not self.parent

	def isLeaf(self):
		return not (self.leftChild or self.rightChild)

	def hasAnyChildren(self):
		return self.rightChild or self.leftChild

	def hasBothChildren(self):
		return self.rightChild and self.leftChild

	def replaceNodeData(self,key,value,lc,rc):
		self.key=key
		self.payload=value
		self.leftChild=lc
		self.rightChild=rc
		if self.hasLeftChild():
			self.leftChild.parent=self
		if self.hasRightChild():
			self.rightChild.parent=self

mytree = BinarySearchTree()
count=0
import itertools
l=list(itertools.permutations([1,2,3]))

for i in range(len(l)):
	for index,j in enumerate(l[i]):
		mytree[index]=j
	count+=1

print count


