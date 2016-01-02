f=open('alice.txt','r')
d={}
l=[]
count=1
for line in f:
	line=line[:-1]
	line=line.lower()
	line=line.split(" ")
	l.append(line)

for i in l:
	for word in i:
		if word in d:
			d[word]+=1
		else:
			d[word]=count

print sorted(d.items())

print sorted(d,key=d.get,reverse=True)[:20]
