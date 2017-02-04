def subset_sum(l, target):
	dp = [[None]*(target+1) for i in range(len(l)+1)]
	
	for i in range(target+1):
		dp[0][i] = False

	for i in range(len(l)+1):
		dp[i][0] = True

	for i in range(1, len(l)+1):
		for j in range(1, target+1):
			# don't include the current element
			dp[i][j] = dp[i-1][j]

			# include the current element only if the target is greater than the last element 
			# and if the previous condition is False
			if dp[i][j] == False and j>=l[i-1]:
				dp[i][j] = dp[i][j] or dp[i-1][j-l[i-1]]

	print dp[len(l)][target]

	i = len(l)
	j = target
	final = []
	while i>0 and j>0:
		if dp[i][j] == True and dp[i-1][j] == False:
			final.append(l[i-1])
			j = j-l[i-1]
		elif dp[i][j] == True and dp[i-1][j] == True:
			i-=1

	print final

subset_sum([1,3,9,2], 5)

