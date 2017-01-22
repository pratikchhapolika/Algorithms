def lengthOfLongestSubstring(s):
	d = {}
	start = -1
	maxL = 0
	
	for i in range(len(s)):
		if s[i] in d:
			start = max(start, d[s[i]])
		
		maxL = max(maxL, i-start)

		d[s[i]] = i
	
	return maxL

print lengthOfLongestSubstring("abcabcbb")
print lengthOfLongestSubstring("c")
print lengthOfLongestSubstring("au")
