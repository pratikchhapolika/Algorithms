def isPalindrome(s):
	s = s.lower()
	i = 0
	j = len(s) - 1
	
	while i<j:
		if s[i] == s[j]:
			i+=1
			j-=1
		elif not s[i].isalnum():
			i+=1
		elif not s[j].isalnum():
			j-=1
		else:
			return False
		
	return True

print isPalindrome("A man, a plan, a canal: Panama")
print isPalindrome("race a car")
