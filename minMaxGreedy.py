# l=[4504,1520,5857,4094,4157,3902,822,6643,2422,7288,8245,9948,2822,1784,7802,3142,9739,5629,5413,7232]
l=[1,2,3,4,10,20,30,40,100,200]


length=input()
k=input()
l=[]
while length>0:
	number=input()
	l.append(number)
	length-=1

def minMax(l,k):
	# p=[]
	# l=sorted(l)
	# q=[]
	# o=[]
	# for i in xrange(len(l)):
	# 	p.append(l[i-1:i+k-1])

	# for i in p:
	# 	if len(i)==k:
	# 		o.append(i)
	

	# for i in o:
	# 	q.append(max(i)-min(i))
	
	# print min(q)
	q=[]
	l=sorted(l)
	i=0
	j=k-1
	while j<len(l):
		q.append(l[j]-l[i])
		i+=1
		j+=1
	print min(q)



minMax(l,k)