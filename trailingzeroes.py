import math
def trailingZeroes(n):
	l=[]
	for i in xrange(1,50):
		a=math.floor(n/(5**i))
		print a
		if a>0:
			l.append(a)
	print int(sum(l))		

trailingZeroes(625)
