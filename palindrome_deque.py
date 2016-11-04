class Deque(object):

	def __init__(self):
		self.items=[]

	def is_empty(self):
		return self.items==[]

	def add_rear(self,item):
		self.items.insert(0,item)

	def add_front(self,item):
		self.items.append(item)

	def remove_rear(self):
		return self.items.pop(0)

	def remove_front(self):
		return self.items.pop()

	def size(self):
		return len(self.items)

def palindrome(str1):
	d=Deque()

	for i in str1:
		d.add_rear(i)

	equal=True

	while d.size()>1 and equal:
		first=d.remove_front()
		last=d.remove_rear()
		# if first==last:
		# 	equal=True
		# 	continue
		if first!=last:
			equal=False
			
	print equal

palindrome("maam")
palindrome("yash")
palindrome("yashh")
palindrome("linkedinnideknil")