# l=[1,1,1,2,2,4]
# p=[3,3,3,6]

l=[-9, -1, -4, 8, 9, 6, -5, -7, 3, 9]
p=[6, 6, 4, -1, 7, -6, -9, 4, -8, 8]

d={}

for i in l:
	d[i]=None

print d

k=(sum(l)-sum(p))//2

for i in range(len(p)):
	inter=p[i]+k
	if inter in d:
		print inter,p[i]