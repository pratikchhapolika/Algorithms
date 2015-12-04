class Node(object):

	def __init__(self,initdata):
		self.data=initdata
		self.next=None

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def setData(self,newdata):
		self.data=newdata

	def setNext(self,newnext):
		self.next=newnext

class OrderList(object):

	def __init__(self):
		self.head=None

	def is_empty(self):
		return self.head==None

	def add(self,data):
		current=self.head
		previous=None
		stop=False

		while current!=None and not stop:
			if current.getData() > data:
				stop=True
			else:
				previous=current
				current=current.getNext()

		temp=Node(data)

		if previous==None:
			temp.setNext(self.head)
			self.head=temp
		else:
			temp.setNext(current)
			previous.setNext(temp)

	def search(self,item):
		current=self.head
		found=False
		stop=False

		while current!=None and not found and not stop:
			if current.getData() == item:
				found=True
			elif current.getData() > item:   # it is to stop the search earlier if the element is not present.
				stop=True
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

	def display(self):
		current=self.head
		
		while current!=None:
			print current.getData()
			current=current.getNext()

mylist=OrderList()
mylist.add(17)
mylist.add(26)
mylist.add(31)
mylist.add(54)
mylist.add(77)
mylist.add(93)
mylist.display()
print mylist.search(45)
