def max_sum(l):
	dp=[None]*len(l)

	for i in range(len(l)):
		if i==0:
			dp[i] = l[0]
		elif i==1:
			dp[i] = max(l[0], l[1])
		else:
			dp[i] = max(l[i]+dp[i-2], dp[i-1])

	return dp[len(l)-1]

print max_sum([1,0,3,9,2])
print max_sum([3,2,5,10,7])
