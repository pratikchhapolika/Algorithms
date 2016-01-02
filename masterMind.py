import random
def guess(a):
	p=[]
	l=['y','r','g','b']
	for i in range(4):
		p.append(random.choice(l))
	str1=''.join(p)
	print str1

	temp=[]
	hit=0
	pseudo_hit=0
	
	for i in xrange(len(a)):
		if a[i]==str1[i]:
			hit+=1
			str1=str1.replace(str1[i],' ')
		
	for i in xrange(len(a)):
		if a[i] in str1:
			temp.append(a[i])
		else:
			continue
	
	temp=[i for i in set(temp)]
	pseudo_hit=len(temp)
	print hit, pseudo_hit

guess("ggrr")
