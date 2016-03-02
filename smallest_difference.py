import sys

l=[2,3,1,236,11,15,129]
p=[23,19,127,8,235]
k=[]

l=sorted(l)
p=sorted(p)

i=0
j=0

m=sys.maxsize

while (i<len(l)) or (j<len(p)):
	if i>=len(l):
		break
	if j>=len(p):
		break

	s=l[i]-p[j]
	if s<0:
		i+=1
	else:
		j+=1

	if s>0:
		if s<m:
			m=s


print m