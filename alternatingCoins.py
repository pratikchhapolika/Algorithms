a=input()

def alternating_coins(a):
	l=[0,1,3]
	for i in range(3,a+1):
		s=l[i-1]+l[i-2]+2
		l.append(s%1000000007)
	print l[a]%1000000007

alternating_coins(a)
