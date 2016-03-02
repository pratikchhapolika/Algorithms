string="aaaabaaa"

def check(s):
	if s==s[::-1]:
		return True

def palindrome(string):
	palin=''
	m=0
	for i in range(1,len(string)+1):
		for j in range(i):
			other=string[j:i]
			flag=check(other)
			if flag:
				if len(other)>=m:
					m=len(other)
					palin=other
	print palin

palindrome(string)