class Queue(object):

	def __init__(self):
		self.items=[]

	def is_empty(self):
		return self.items==[]

	def enqueue(self,item):
		self.items.insert(0,item)

	def dequeue(self):
		return self.items.pop()

	def size(self):
		return len(self.items)

# q=Queue()
# q.enqueue(5)
# q.enqueue('hello')
# q.enqueue('dog')
# q.enqueue(3)
# print q.dequeue()
# print q.items
