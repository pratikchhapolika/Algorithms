class Node(object):

	def __init__(self,initdata):
		self.data=initdata
		self.next=None

class LinkedList:
 
	# Function to initialize head
	def __init__(self):
		self.head = None
 
	# Function to insert a new node at the beginning
	def add(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	def add_last(self, new_data):
		tail = None
		current = self.head

		while current!=None and current.next!=None:
			current=current.next
		tail = current
		
		new_node = Node(new_data)
		tail.next = new_node
		tail = new_node

	def display(self):
		current = self.head
		while current!=None:
			print current.data,
			current=current.next

	def gettail(self):
		tail = None
		current = self.head

		while current!=None and current.next!=None:
			current=current.next
		tail = current
		return tail

	def remove(self,item):
		current=self.head
		found=False
		previous=None

		while not found:
			if current.data == item:
				found=True
			else:
				previous=current
				current=current.next

		if previous==None:
			self.head=current.next
		else:
			previous.next = current.next

	def segregate(self):
		l=[]
		current = self.head
		while current!=None:
			if current.data%2!=0:
				l.append(current.data)
				self.remove(current.data)
			current = current.next
		return l

mylist=LinkedList()
mylist.add(6)
mylist.add(7)
mylist.add(1)
mylist.add(4)
mylist.add(5)
mylist.add(10)
mylist.add(12)
mylist.add(8)
mylist.add(15)
mylist.add(17)

p = []
p = mylist.segregate()

for i in p:
	mylist.add_last(i)

mylist.display()