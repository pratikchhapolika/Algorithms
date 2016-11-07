# Given a string S, you are allowed to convert it to a palindrome by adding characters in front of it. 
# Find and return the shortest palindrome you can find by performing this transformation.

# For example:

# Given "aacecaaa", return "aaacecaaa".

# Given "abcd", return "dcbabcd".

# Its an O(n^2) solution but runs faster than most of the C solutions.

def shortestPalindrome(s):
	r = s[::-1]
	for i in range(len(s) + 1):
		if s.startswith(r[i:]):
			return r[:i] + s

print shortestPalindrome('aacecaaa')
print shortestPalindrome('abcd')
print shortestPalindrome('maam')
