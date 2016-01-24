from graph import Graph

def Connected():  #bdsize is the board size
	m=Graph()
	f=open('grid.txt','r')
	l=[i[:-1] for i in f]
	length=len(l[0])

	for row in range(length):
		for col in range(length):
			if l[row][col]!='0':
				nodeId=posToNodeId(row,col,length)
				newPositions=genLegalMoves(row,col,length)
				for i in newPositions:
					nid=posToNodeId(i[0],i[1],length)
					if l[i[0]][i[1]]!='0':
						m.addEdge(nodeId,nid)
	f.close()
	return m

def posToNodeId(row,col,length):
	return (row*length)+col

def genLegalMoves(x,y,length):
	newMoves=[]
	moveOffsets = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,1),(-1,-1),(1,-1)]
	for i in moveOffsets:
		newX=x+i[0]
		newY=y+i[1]
		if legalCoord(newX,length) and legalCoord(newY,length):
			newMoves.append((newX,newY))
	return newMoves

def legalCoord(x,length):
	if x>=0 and x<length:
		return True
	else:
		return False

temp=[]
g=Connected()
for i in g:
	# temp.append(i.id)
	print i

# print len(temp)