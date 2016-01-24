def anagrams(a,b):
	dict1={}
	dict2={}
	a=sorted(a)
	b=sorted(b)
	count=0

	if a==b:
		return count

	if all(a)!=all(b):
		print "hi"

	for i in a:
		if i in dict1:
			dict1[i]+=1
		else:
			dict1[i]=1

	for i in b:
		if i in dict2:
			dict2[i]+=1
		else:
			dict2[i]=1

	for key1,val1 in dict1.items():
		if key1 in dict2:
			if abs(val1-dict2[key1])!=0:
				count+=abs(val1-dict2[key1])
		else:
			count+=val1

	for key2,val2 in dict2.items():
		if key2 not in dict1:
			count+=val2

	return count

print anagrams("aaa","bbb")