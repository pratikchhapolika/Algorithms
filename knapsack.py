def Knapsack(W,wtList,valList,n):
	l=[[None]*(W+1) for i in range(n+1)]

	for i in range(n+1):
		for j in range(W+1):
			if i==0 or j==0:
				l[i][j]=0
			elif wtList[i-1]>W:
				# return Knapsack(W,wtList,valList,n-1)
				l[i][j]=l[i-1][j]
			else:
				# return max(Knapsack(W,wtList,valList,n-1),wtList[n-1]+Knapsack(W-wtList[n-1],wtList,valList,n-1))
				l[i][j]=max(l[i-1][j], wtList[i-1]+l[i-1][j-wtList[i-1]])

	print l[n][W]

W=150
wtList=[10,40,70]
valList=[5,12,15]
n=len(valList)
Knapsack(W,wtList,valList,n)