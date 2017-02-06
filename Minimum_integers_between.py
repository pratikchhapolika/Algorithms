# You need to find the minimum number of integers between x and y.
# For example l = [1,2,'3',9,10,11,'6',13,15,'3'], x=3, y=6
# The integers between 3 and 6 are:- (9,10,11), (13,15)
# Hence the output is 2.

# As x and y can be repeated so that's why we use 2 pointers technique

def minimum_integers_between(l, x, y):
	i = 0
	j = 0
	m = 999999
	while i<len(l) and j<len(l):
		if l[i] == x or l[i] == y:
			count = 0
			while j<len(l) and l[j] != x and l[j] != y:
				count+=1
				j+=1

			if j>=len(l):
				count = 999999

			m = min(m, count)

		i = j
		j+=1

	print m

minimum_integers_between([1,2,3,9,10,11,6,13,15,3], 3, 6)
minimum_integers_between([1,2,3,9,10,11,6,13,3,4,5,6,1], 3, 6)

