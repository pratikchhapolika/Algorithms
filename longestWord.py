# def many(l):
# 	a=[]
# 	b=[]
# 	for i in range(1,len(l)+1):
# 		for j in range(i):
# 			a.append(''.join(l[j:i])) 

# 	k=l[::-1]
# 	for i in range(1,len(k)+1):
# 		for j in range(i):
# 			b.append(''.join(k[j:i]))


# 	return a+b

# def longest(l):
# 	new={}
# 	combo=[]
# 	p=[]
# 	for i in range(len(l)):
# 		rest=l[:i]+l[i+1:]
# 		for j in rest:
# 			combo.append(l[i]+j)
	
# 	new_combo=many(l)

# 	a=new_combo+combo
# 	for i in set(a):
# 		p.append(i)

# 	for i in p:
# 		print i
# 		if i in l:
# 			new[i]=len(i)

# 	print max(new,key=new.get)
# 	print new


def longest(l):
	new={}
	combo=[]
	p=[]
	for i in range(len(l)):
		rest=l[:i]+l[i+1:]
		for j in rest:
			combo=l[i]+j
			if combo in l:
				new[combo]=len(combo)
	print new
	print max(new,key=new.get)

longest(['cat','banana','dog','nana','walk','walker','dogwalker','dognana'])

