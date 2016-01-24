def panagram(string):
	l=[None]*26
	string=string.replace(' ','').lower()
	flag=True
	for i in string:
		l[ord(i)-97]=flag

	if None in l:
		print 'not pangram'
	else:
		print 'pangram'

a=raw_input()
panagram(a)