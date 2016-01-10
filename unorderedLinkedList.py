class Node(object):

	def __init__(self,initdata):
		self.data=initdata
		self.next=None

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def setNext(self,newnext):
		self.next=newnext

class UnorderedList(object):

	def __init__(self):
		self.head=None

	def is_empty(self):
		return self.head==None

	def add(self,data):
		temp=Node(data)
		temp.setNext(self.head)
		self.head=temp

	def search(self,item):
		current=self.head
		found=False

		while current!=None and not found:
			if current.getData() == item:
				found=True
			else:
				current=current.getNext()
		return found

	def size(self):
		current=self.head
		count=0

		while current!=None:
			count+=1
			current=current.getNext()
		print "The size of the linked list is:",count

	def remove(self,item):
		current=self.head
		found=False
		previous=None

		while not found:
			if current.getData() == item:
				found=True
			else:
				previous=current
				current=current.getNext()

		if previous==None:
			self.head=current.getNext()
		else:
			previous.setNext(current.getNext())

	def reverse(self):
		current=self.head
		previous=None
		next=None

		while current!=None:
			next=current.getNext()
			current.setNext(previous)     # reverse statement
			previous=current
			current=next

		self.head=previous

	def display(self):
		current=self.head
		
		while current!=None:
			print current.getData()
			current=current.getNext()

	def index(self,k):
		current=self.head
		count=0
		while current!=None:
			count+=1
			current=current.getNext()
			if count==k:
				break
		if k==0:
			self.display()

		new=current
		while new!=None:
			print new.getData()
			new=new.getNext()



# mylist=UnorderedList()
# mylist.add(31)
# mylist.add(77)
# mylist.add(17)
# mylist.add(93)
# mylist.add(26)
# mylist.add(54)
# mylist.display()
# print
# print mylist.search(77)
# mylist.size()
# mylist.remove(17)
# mylist.display()
# print "The reversed linked list is:"
# mylist.reverse()
# mylist.display()
# print
# mylist.index(1)



