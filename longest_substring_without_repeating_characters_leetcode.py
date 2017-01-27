# Given a string, find the length of the longest substring without repeating characters.

# Examples:

# Given "abcabcbb", the answer is "abc", which the length is 3.

# Given "bbbbb", the answer is "b", with the length of 1.

# Given "pwwkew", the answer is "wke", 
# with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.



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
