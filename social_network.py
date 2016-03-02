# def root(i):
# 	while l[i]!=i:
# 		i=l[i]
# 	return i

# def union(a,b):
# 	root_a=root(a)
# 	root_b=root(b)
# 	l[root_a]=root_b

def union(a,b):
	temp=l[a]
	for i in range(len(l)):
		if l[i]==temp:
			l[i]=l[b]

def find(a,b):
	# if root(a)==root(b):
	# 	return 'YES'
	# return 'NO'

	if l[a]==l[b]:
		return 'YES'
	return 'NO'

def initialize(l):
	for i in range(len(l)):
		l[i]=i

# l=[None]*6
# initialize(l)
# union(1,2)
# union(2,3)
# union(4,1)
# union(4,5)

# print find(1,3)
# print find(1,4)
# print find(1,5)
# print l

a=raw_input()
n,f=map(int,a.split())
l=[None]*(n+1)
initialize(l)
d={}

while f>0:
	b = raw_input()
	choice,f1,f2 = b.split()

	if choice=='A':
		union(int(f1),int(f2))
	else:
		d[int(f1)]=int(f2)
	f-=1

q=input()
p=[]
while q>0:
	b1 = raw_input()
	friend1,friend2=map(int, b1.split())

	if friend1 in d:
		if d[friend1]==friend2:
			p.append('YES')

	elif friend2 in d:
		if d[friend2]==friend1:
			p.append('YES')

	else:
		p.append(find(friend1,friend2))
	
	q-=1

cn=0
cp=0
for i in p:
	if i=='NO':
		cn+=1
	else:
		cp+=1

print cn,cp





