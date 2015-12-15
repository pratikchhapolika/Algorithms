from graph import Graph,Vertex
from queue import Queue


def Maze(bdsize):  #bdsize is the board size
	m=Graph()
	for row in range(bdsize):
		for col in range(bdsize):
			nodeId=posToNodeId(row,col,bdsize)
			newPositions=genLegalMoves(row,col,bdsize)
			for i in newPositions:
				nid=posToNodeId(i[0],i[1],bdsize)
				if nid!=12 and nid!=11 and nid!=10:
					m.addEdge(nodeId,nid)

	return m

def posToNodeId(row,col,bdsize):
	return (row*bdsize)+col

def genLegalMoves(x,y,bdsize):
	newMoves=[]
	moveOffsets = [(1,0),(0,1),(-1,0),(0,-1)]
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

def BFS(g,start):  # g is the graph and start is the starting vertex
	start.setDistance(0)
	start.setPredecessor(None)
	verticesQueue=Queue()
	verticesQueue.enqueue(start)
	while verticesQueue.size()>0:
		currentVertex=verticesQueue.dequeue()
		for nbr in currentVertex.getConnections():
			if nbr.getColor()=='white':
				nbr.setColor('gray')
				nbr.setDistance(currentVertex.getDistance()+1)
				nbr.setPredecessor(currentVertex)
				verticesQueue.enqueue(nbr)
		currentVertex.setColor('black')


g=Maze(5)

start=g.getVertex(24)

BFS(g,start)

def traverse(y):
	x=y
	while x.getPredecessor():
		print x.id, x.getDistance()
		x=x.getPredecessor()
	print x.id, x.getDistance()

traverse(g.getVertex(0))