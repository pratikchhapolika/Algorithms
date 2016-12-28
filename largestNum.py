from fractions import Fraction
def compare(a,b):
	if int(str(a)+str(b))>int(str(b)+str(a)):
		return str(a)+str(b)
	else:
		return str(b)+str(a)



def largestnum(l):
	# if all(l)==0:
	# 	return 0
	# c=l[0]
	# for i in range(1,len(l)):
	# 	c=compare(c,l[i])
	# return c

	l=sorted(l, key=lambda n: Fraction(n, 10**len(str(n))), reverse=True)
	print l
	

largestnum([472,663,964,722,485,852,635,4,368,676,319,412])

