# Find all palindromes in a given string
# Time complexity:- O(n^2)
string='aaaabaaa'
result=''
final=[]
length=len(string)

def checkPalindrome(result,s,i,j):
	while i>=0 and j<length and s[i]==s[j]:
		result=s[i:j+1]
		i-=1
		j+=1
		final.append(result)

for i in range(length):
	# for even length palindromes
	checkPalindrome(result,string,i,i+1)
	# for odd length palindromes
	checkPalindrome(result,string,i,i)

print max(set(final), key=len)
