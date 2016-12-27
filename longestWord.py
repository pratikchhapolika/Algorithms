def unscramble(s,d):
	i=0
	j=0
	l=[]
	length = len(s)
	while j<length:
		r = s[i:j+1]
		if r in d and j==length-1:
			return
		if r not in d:
			j+=1

		else:
			temp = j
			j+=1
			while j<length:
				temp_r = s[i:j+1]
				if temp_r not in d:
					j+=1
				else:
					temp = j
					j+=1

			l.append(s[i:temp+1])
			j = temp+1
			i = j

	print l


def longest(l):
	d={}
	m=0
	p=[None]
	for i in l:
		d[i]=True
	
	# for i in l:
	# 	for j in range(1,len(i)):
	# 		left = i[:j]
	# 		right = i[j:]

	# 		if left in d and right in d:
	# 			if len(i)>m:
	# 				m = len(i)
	# 				p.pop()
	# 				p.append(i)

	for i in l: 
		unscramble(i, d)


	# print m, p
			

longest(['cat','banana','dog', 'dogs','nana','walk','walker','catdogswalker','dognana'])

