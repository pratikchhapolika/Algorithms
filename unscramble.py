def unscramble(s,d):
	i=0
	j=0
	l=[]
	length = len(s)
	while j<length:
		r = ''.join(sorted(s[i:j+1]))
		if r not in d.keys():
			j+=1
		else:
			temp = j
			j+=1
			while j<length:
				temp_r = ''.join(sorted(s[i:j+1]))
				if temp_r not in d:
					j+=1
				else:
					temp = j
					j+=1

			l.append(d[''.join(sorted(s[i:temp+1]))])
			j = temp+1
			i = j

	print l


dictionary = ['hello', 'an', 'to', 'apple', 'the', 'world', 'a', 'orange', 'hell']

l=[]
d={}
for i in dictionary:
	d[''.join(sorted(i))] = i

unscramble('elhloothtedrowl', d)
unscramble('ppela', d)
unscramble('nappela', d)
unscramble('ppelaaana', d)
unscramble('ppelb', d)



