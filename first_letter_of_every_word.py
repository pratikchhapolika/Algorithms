s = ' this    is     a   test     case   ' 
i=0

if s[0]!=' ':
	print s[0],
while i<len(s) and i+1<len(s):
	if s[i]==' ' and s[i+1]!=' ':
		print s[i+1],
		i+=1
	else:
		i+=1