def editDistance(str1, str2, n, m):
	dp = [[0 for j in range(m+1)] for i in range(n+1)]

	for i in range(n+1):
		for j in range(m+1):
			if i==0:
				dp[i][j] = j
			elif j==0:
				dp[i][j] = i
			elif str1[i-1] == str2[j-1]:
				dp[i][j] = dp[i-1][j-1]
			else:
				dp[i][j] = 1 + min(dp[i-1][j],   #remove
								   dp[i][j-1],   #insert
								   dp[i-1][j-1]) #replace
	print dp[n][m]

str1 = "sunday"
str2 = "saturday"

editDistance(str1, str2, len(str1), len(str2))