# A secret message containing letters from A-Z is being encoded to numbers using the following mapping:
# 'A' -> 1
# 'B' -> 2
# .
# .
# 'Z' -> 26

# You are given a sequence of digits. 
# Determine the total number of ways the message can be decoded.
# Example:- Input: digits{1,2,3} Output: 3 (All possible interpretations are 'ABC' 'LC' 'AW')

def decode(s):
	dp = [0 for i in range(len(s))]
	s = map(int, list(s))

	if s[0]>0:
		dp[0]+=1

	for i in range(1,len(s)):
		if s[i]>0:
			dp[i]+=dp[i-1]
		if (s[i-1]*10 + s[i]<=26) and (s[i-1]*10 + s[i]>=10):
			if i==1:
				dp[i]+=1
			else:
				dp[i]+=dp[i-2]

	print dp[len(s)-1]

decode('26')