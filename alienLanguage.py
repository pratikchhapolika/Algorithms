import re
words=['abc','bca','dac','dbc','cba','tree','used']

# string='(ab)(bc)(ca)'
# string='abc'
# string='(abc)(abc)(abc)'
# string='(zyx)bc'
string='(tuv)(pqrs)(def)(def)'

string=string.replace('(','[').replace(')',']')

# this will return every possible combination of string
r=re.compile(string).search  

# this will give the intersection of r with words
print filter(r,words)