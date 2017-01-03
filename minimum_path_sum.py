def minPathSum(grid):
	row = len(grid)
	col = len(grid[0])
		
	dp = [[None for j in range(col)] for i in range(row)]
		
	for i in range(row):
		for j in range(col):
			if i==0 and j==0:
				dp[i][j] = grid[i][j]
			elif i==0 and j>0:
				dp[i][j] = dp[0][j-1] + grid[i][j]
			elif i>0 and j==0:
				dp[i][j] = dp[i-1][0] + grid[i][j]
			else:
				dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
		
	return dp[row-1][col-1]

print minPathSum([[0]])