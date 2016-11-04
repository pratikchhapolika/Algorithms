# O(n^2) solution using brute force
# def pairs(l,k):
# 	p=[]
# 	l=sorted(l)
# 	for i in range(len(l)-1):
# 		j=len(l)-1
# 		while j>i:
# 			if abs(l[i]-l[j])==k:
# 				p.append([l[i],l[j]])
# 				break
# 			j-=1
# 	print len(p)

# a=raw_input()
# length,k=map(int,a.split())
# b = raw_input()
# array = map(int, b.split())


# O(nlogn) solution using 2 pointers 
# def pairs(l,k):
	# p=[]
	# l=sorted(l)
	
	# 1st method
	# i=0
	# j=0
	
	# size=len(l)
	
	# 2nd method
	# i=0
	# j=size-1

	# 1st method
	# while i!=size and j!=size:
	# 	if abs(l[j]-l[i])==k:
	# 		p.append([l[i],l[j]])
	# 		i+=1
	# 		j+=1
	# 	elif abs(l[j]-l[i])>k:
	# 		j+=1
	# 	else:
	# 		i+=1

	# 2nd method
	# while i<size and j<size:
	# 	if l[j]-l[i]==k:
	# 		print l[j],l[i]
	# 		i+=1
	# 		j+=1
	# 	elif l[j]-l[i]>k:
	# 		j-=1
	# 	else:
	# 		i+=1

	# print p

# a=raw_input()
# length,k=map(int,a.split())
# b = raw_input()
# array = map(int, b.split())

# pairs(array,k)


# O(nlogn) solution using binary search
# def binary_search(l,start,end,x):
# 	while start<=end:
# 		mid=start+(end-start)/2
# 		if l[mid]==x:
# 			return l[mid]
# 		elif x<l[mid]:
# 			end=mid-1
# 		else:
# 			start=mid+1
# 	return False

# def pairs(l,k):
# 	p=[]
# 	l=sorted(l)
# 	for i in range(len(l)):
# 		temp=binary_search(l,i+1,len(l)-1,(l[i]+k))
# 		if temp!=False:
# 			p.append([l[i],temp])
# 	print len(p)

# l=[1,5,3,4,2]
# k=0
# pairs(l,k)


# O(n) solution using dictionary
def pairs(l,k):
	p=[]
	d={}
	for i in set(l):
		d[i]=1
	
	for key in d.keys():
		if key+k in d:
			p.append([key,key+k])

	print p

l=[8, 12, 16, 4, 0, 20]
k=4
pairs(l,k)
