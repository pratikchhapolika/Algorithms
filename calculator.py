# string='2*3+12/4*3+15'
# string='5/5+1+8/4+8*8+4-2/1*9'
string='2-6-7*8/2+5'

# string='6/5*3+4*5/2-12/6*3/3+3+3'
l=[]
p=[]
q=[]
r=[]

# evaluating the '/' first
i=0
while i<len(string):
	if string[i]!='/':
		l.append(string[i])
	else:
		temp1=[]
		a=l[-1]
		while (a!='+') or (a!='-') or (a!='/') or (a!='*'):
			temp1.insert(0,l.pop())
			if len(l)!=0:
				a=l[-1]
			else:
				break
			if a=='+' or a=='-' or a=='/' or a=='*' or a=='':
				break

		temp2=''
		b=string[i+1]
		while (b!='+') or (b!='-') or (b!='/') or (b!='*'):
			temp2+=b
			i+=1
			if i<len(string)-1:
				b=string[i+1]
			else:
				break
			if b=='+' or b=='-' or b=='/' or b=='*':
				break

		l.append(str(int(''.join(temp1))/int(temp2)))
	i+=1

# evaluating '*' 
j=0
while j<len(l):
	if l[j]!='*':
		p.append(l[j])
	else:
		temp1=[]
		a=p[-1]
		while (a!='+') or (a!='-') or (a!='/') or (a!='*'):
			temp1.insert(0,str(p.pop()))
			if len(p)!=0:
				a=p[-1]
			else:
				break
			if a=='+' or a=='-' or a=='/' or a=='*' or a=='':
				break

		temp2=''
		b=l[j+1]
		while (b!='+') or (b!='-') or (b!='/') or (b!='*'):
			temp2+=b
			j+=1
			if j<len(l)-1:
				b=l[j+1]
			else:
				break
			if b=='+' or b=='-' or b=='/' or b=='*':
				break

		p.append(int(''.join(temp1))*int(temp2))
	j+=1



# + and - have the same priority
# evaluating '+' and '-'
result=eval(''.join(map(str,p)))
print result