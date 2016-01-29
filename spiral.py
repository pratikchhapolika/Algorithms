l=[[1,2,3,4,5],
   [6,7,8,9,10],
   [11,12,13,14,15],
   [16,17,18,19,20],
   [21,22,23,24,25]]


# l=[[1,2,3,4],
#    [5,6,7,8],
#    [9,10,11,12],
#    [13,14,15,16]]

# l=[[1,2,3],
#    [4,5,6],
#    [7,8,9]]

r=0
c=0
row=len(l[0])
col=len(l)
lastr=row-1
lastc=col-1
p=[]
while row>1 and col>1:
	for i in range(col):
		if l[r][i] not in p:
			p.append(l[r][i])
			print l[r][i],	
	
	for i in range(row):
		if l[i][lastc] not in p:
			p.append(l[i][lastc])
			print l[i][lastc],
	
	for i in range(col-1,-1,-1):
		if l[lastr][i] not in p:
			p.append(l[lastr][i])
			print l[lastr][i],
	
	for i in range(row-1,-1,-1):
		if l[i][c] not in p:
			p.append(l[i][c])
			print l[i][c],

	r+=1
	c+=1
	lastr-=1
	lastc-=1
	row-=1
	col-=1
