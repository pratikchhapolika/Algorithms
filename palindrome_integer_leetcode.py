def isPalindrome(x):
	if x<0:
		return False
	
	msb = 0
	div = 1
	# Gets the first 2 digits
	while x/div >= 10:
		msb = x/div
		div*=10

	while x>0:
		lsb = x%10
		msb = x/div

		if msb != lsb:
			return False
		else:
			# Removes the msb and the lsb
			x = (x%div)/10
			# shorten the div since we are removing
			# the first and the last digit
			div = div/100

	return True


print isPalindrome(1000021)
print isPalindrome(1221)
print isPalindrome(1223)
print isPalindrome(1)
print isPalindrome(3)
