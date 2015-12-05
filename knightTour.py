from graph import Graph,Vertex

def knightGraph(bdsize):  #bdsize is the board size
	ktgraph=Graph()
	for row in range(bdsize):
		for col in range(bdsize):
			nodeId=posToNodeId(row,col,bdsize)
			newPositions=genLegalMoves(row,col,bdsize)
			for i in newPositions:
				nid=posToNodeId(i[0],i[1],bdsize)
				ktgraph.addEdge(nodeId,nid)

	return ktgraph

def posToNodeId(row,col,bdsize):
	return (row*bdsize)+col

def genLegalMoves(x,y,bdsize):
	newMoves=[]
	moveOffsets = [(-1,-2),(-1,2),(-2,-1),(-2,1),( 1,-2),( 1,2),( 2,-1),( 2,1)]
	for i in moveOffsets:
		newX=x+i[0]
		newY=y+i[1]
		if legalCoord(newX,bdsize) and legalCoord(newY,bdsize):
			newMoves.append((newX,newY))
	return newMoves

def legalCoord(x,bdsize):
	if x>=0 and x<bdsize:
		return True
	else:
		return False

def orderByAvail(n):    # used instead of u.getConnections()
	resList = []		
	for v in n.getConnections():
		if v.getColor() == 'white':
			c = 0
			for w in v.getConnections():
				if w.getColor() == 'white':
					c = c + 1
			resList.append((c,v))
	resList.sort(key=lambda x: x[0])
	return [y[1] for y in resList]

def knightTour(n,path,u,limit):  # DFS ALGORITHM
	# u is the vertex in the graph we wish to explore
	# n is the current depth in the search tree
	# path is a list of vertices visited up to this point
	# limit is the number of nodes in the path
	u.setColor('gray')
	path.append(u)     # list 
	if n<limit:
		vertexList=orderByAvail(u)    # replacement for list(u.getConnections())
		i=0
		done=False     # it signifies whether the entire graph is traversed or not
		while i<len(vertexList) and not done:
			if vertexList[i].getColor()=='white':
				done=knightTour(n+1,path,vertexList[i],limit)
			i=i+1
		if not done:      # this is for backtracking
			path.pop()
			u.setColor('white')

	else:
		done=True

	return done

board_size=input("Enter the board size\n")
k=knightGraph(board_size)
for i in k:
	print i
print
u=k.getVertex(0)
print knightTour(0,[],u,(board_size**2)-1)

