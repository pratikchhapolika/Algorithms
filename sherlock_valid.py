def sherlock(string):
	d={}
	keyslist=[]
	p=[]
	for i in string:
		if i in d:
			d[i]+=1
		else:
			d[i]=1

	keyslist=d.values()
	for i in range(len(keyslist)):
		other=keyslist[:i]+keyslist[i+1:]
		if all(other[i] == other[i+1] for i in range(len(other)-1)):
			p.append("YES")
		else:
			p.append("NO")

	if "YES" in p:
		print "YES"
	else:
		print "NO"

string=raw_input()

sherlock(string)