n=3
def paran(p,i):
	if i<n:
		paran('()'+p,i+1)
		paran('('+p+')',i+1)
		if p[:2]!='()':
			paran(p+'()',i+1)
	else:
		print p

paran('()',1)