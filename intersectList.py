class Solution:
	# @param A : head node of linked list
	# @param B : head node of linked list
	# @return the head node in the linked list
	def length(self,a):
		l=0
		while a:
			l+=1
			a=a.next
		return l
		
	def getIntersectionNode(self, A, B):
		la=self.length(A)
		lb=self.length(B)
		a=A
		b=B
		
		while a and b:
			if la>lb:
				la-=1
				a=a.next
			elif lb>la:
				lb-=1
				b=b.next
			else:
				if a==b:
					return a
				else:
					a=a.next
					b=b.next