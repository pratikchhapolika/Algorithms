# Majority Element: A majority element in an array A of size n is an 
# element that appears more than n/2 times (and hence there is at most one such element).

def majority_element(l):
	count = 0
	candidate = 0
	majority = 0

	for i in l:
		if count == 0:
			candidate = i
		elif i == candidate:
			count+=1
		else:
			count-=1

	# to check if the candidate found 
	# is in majority or not
	for i in l:
		if i==candidate:
			majority+=1
	
	if majority>len(l)/2:
		print candidate
	else:
		print -1

	

majority_element([3,3,4,2,4,4,2,4,4])
majority_element([3,3,4,2,4,4,2,4])
majority_element([1,3,3,1,2])
