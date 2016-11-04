def perc_down(i,size,heapList):
	while i*2<=size:
		mc=min_child(i,size,heapList)
		if heapList[i]>heapList[mc]:
			heapList[i],heapList[mc]=heapList[mc],heapList[i]
		i=mc

def min_child(i,size,heapList):
	if i*2+1 > size:
		return i*2
	else:
		if heapList[i*2]<heapList[i*2+1]:
			return i*2
		else:
			return i*2+1

def buildHeap(l):
	i=len(l)//2
	size=len(l)
	heapList=[0]+l[:]
	while i>0:
		perc_down(i,size,heapList)
		i=i-1
	return heapList

def del_min(heapList):
	size=len(heapList)-1
	min_value=heapList[1]
	heapList[1]=heapList[size]
	heapList.pop()
	size-=1
	perc_down(1,size,heapList)
	return min_value

l=[9,5,6,2,3]
h=buildHeap(l)
print h
print del_min(h)
print del_min(h)
print del_min(h)
print del_min(h)
print del_min(h)
