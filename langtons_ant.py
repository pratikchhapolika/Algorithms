def ant(k):
	# 1=white
	# 0=black
	grid=[[1,1,1,1],
		  [1,0,0,0],
		  [0,0,0,1],
		  [1,1,0,1]]

	length=len(grid)
	
	ant_pos=5
	a,b=nodeToPosId(ant_pos,length)

	direction='right'

	while k>0 and a>=0 and a<length and b>=0 and b<len(grid[0]):
		if grid[a][b]==1:
			grid[a][b]=0
			if direction=='right':
				a,b=a+1,b
				direction='down'
			elif direction=='down':
				a,b=a,b-1
				direction='left'
			elif direction=='left':
				a,b=a-1,b
				direction='up'
			else:
				a,b=a,b+1
				direction='right'

		elif grid[a][b]==0:
			grid[a][b]=1
			if direction=='right':
				a,b=a-1,b
				direction='up'
			elif direction=='up':
				a,b=a,b-1
				direction='left'
			elif direction=='left':
				a,b=a+1,b
				direction='down'
			else:
				a,b=a,b+1
				direction='right'

		k-=1

	print grid


def nodeToPosId(nid,length):
	row=nid//length
	col=nid%length
	return row,col

ant(5)


