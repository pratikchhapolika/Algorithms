d=[None,None,['a','b','c'],['d', 'e', 'f'],['g', 'h', 'i'],['j', 'k', 'l'],
	['m', 'n', 'o'],['p', 'q', 'r', 's'],['t', 'u', 'v'],['w', 'x', 'y', 'z']]

def valid(number,index,word):
	if index==len(number):
		print word
		return
	else:
		digit=number[index]
		letters=d[int(digit)]
		for letter in letters:
			valid(number,index+1,word+letter)
word=""
valid("8733",0,word)
