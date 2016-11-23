def anagram_substring(string, pattern):
	string_count = [0]*256
	pattern_count = [0]*256

	for i in range(len(pattern)):
		pattern_count[ord(pattern[i])]+=1
		string_count[ord(string[i])]+=1
	
	for i in range(len(pattern), len(string)):
		if string_count==pattern_count:
			print i-len(pattern)

		# instead of calculating the count of the 
		# window again and again, just remove the
		# first character of the window and 
		# add the next character into string_count list

		# adding the current character of string to string_count list
		string_count[ord(string[i])]+=1

		# removing the first character of the window
		string_count[ord(string[i-len(pattern)])]-=1

	if string_count==pattern_count:
		print len(string) - len(pattern)


anagram_substring('forxxorfxdfro', 'for')
anagram_substring('dddddaaa', 'dad')