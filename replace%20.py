def re(l,length):
	while length>0: 
		if l[0]!=" ":
			l.append(l[0])
		else:
			l.append("%20")
		
		l.remove(l[0])
		length-=1
	return ''.join(l)

string="My name is Yash Katariya"
l=list(string)
length=len(l)

print re(l,length)