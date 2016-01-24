def t2sum(l,target):
	small=0
	large=len(l)-1
	while small<large:
		s=l[small]+l[large]
		if s==target:
			return True
		elif s<target:
			small+=1
		else:
			large-=1
	return False

l=[9,10,20]
target=19

print t2sum(l,target)