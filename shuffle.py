from random import randint

def Shuffle(l):
	p=[]
	n=len(l)-1
	for i in range(n):
		r=randint(0,n)
		l[i],l[r]=l[r],l[i]
	return l
	
print Shuffle([1,2,3,4,5,6])