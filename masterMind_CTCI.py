import random
def mind(guess):
	p=[]
	l=['y','r','g','b']
	for i in range(4):
		p.append(random.choice(l))
	actual=''.join(p)
	print actual

	# actual = 'rgby'

	temp=[]
	hit=0
	pseudo_hit=0
	d={}
	
	for i in xrange(len(guess)):
		if guess[i]==actual[i]:
			hit+=1
		else:
			if actual[i] in d:
				d[actual[i]]+=1
			else:
				d[actual[i]]=1

	for i in guess:
		if i in d and d[i]>0:
			pseudo_hit+=1
			d[i]-=1
	
	
	print hit, pseudo_hit

mind("ggrr")
