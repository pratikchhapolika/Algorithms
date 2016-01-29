test=input()
l=[]
while test>0:
	x=input()
	def flip(x):
		string=bin(x)[2:].zfill(32)
		ib_string = ""

		for bit in string:
		  if bit == "1":
		    ib_string += "0"
		  else:
		    ib_string += "1"

		return int(ib_string,2)

	l.append(flip(x))
	test-=1

for i in l:
	print i