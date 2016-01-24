string="aabcccccaaa"
count=1
first=string[0]
str1=""
for i in range(1,len(string)):
	if first==string[i]:
		count+=1
	else:
		str1+=first+str(count)
		first=string[i]
		count=1

print str1+first+str(count)