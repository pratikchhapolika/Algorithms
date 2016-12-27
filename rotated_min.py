def rotate(l):
	low=0
	high=len(l)-1
	while low<=high:
		mid=(low+high)/2
		if low==high and high==mid and low==mid:
			return l[mid]
		if l[mid]<=l[mid-1] and l[mid]<=l[mid+1]:
			return l[mid]
		elif l[low]>l[high] and l[mid]>=l[low]:
			low=mid+1
		else:
			high=mid-1

	return "Number not found"

print rotate([1,2,3,4,5,6])
print rotate([6,1,2,3,4,5])
print rotate([5,6,1,2,3,4])
print rotate([4,5,6,1,2,3])
print rotate([3,4,5,6,1,2])
print rotate([2,3,4,5,6,1])
print rotate([490,600,80,91,300,390])
print rotate([2,1])

