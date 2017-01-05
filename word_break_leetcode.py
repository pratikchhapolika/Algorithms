def wordBreak(s, wordDict):
	dp = [False] * (len(s)+1)
	dp[0] = True
		
	for i in range(len(s)):
		for j in range(i, len(s)):
			if dp[i]==True and s[i:j+1] in wordDict:
				print dp
				dp[j+1]=True
		
	return dp[-1]

wordBreak('leetcode', ['leet', 'code'])