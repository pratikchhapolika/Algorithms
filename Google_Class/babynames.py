import re
l=[]
f=open('baby1990.html','r')
text=f.read()
a=re.search(r'Popularity in (\d{4})', text)
year=a.group(1)
l.append(year)
tuples=re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', text)

d={}
for i in tuples:
	(rank,boy,girl)=i
	if boy not in d:
		d[boy]=rank
	if girl not in d:
		d[girl]=rank

for i in d:
	print d[i],i

for i in tuples:
	l.append((i[0],i[1]))
	l.append((i[0],i[2]))

print l