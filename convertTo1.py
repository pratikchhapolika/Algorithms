memo={}
def getmin(n):
	if n==1:
		return 0
	if n in memo:
		return memo[n]
	r=1+getmin(n-1)
	if n%2==0:
		r=min(r,1+getmin(n/2))
	elif n%3==0:
		r=min(r,1+getmin(n/3))

	memo[n]=r
	return r

print getmin(4)