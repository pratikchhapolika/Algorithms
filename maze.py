from graph import Graph,Vertex
from queue import Queue


def Maze():  #bdsize is the board size
	m=Graph()
	f=open('board.txt','r')
	l=[i[:-1] for i in f]
	length=len(l[0])

	for row in range(length):
		for col in range(length):
			if l[row][col]!='7':
				nodeId=posToNodeId(row,col,length)
				newPositions=genLegalMoves(row,col,length)
				for i in newPositions:
					nid=posToNodeId(i[0],i[1],length)
					m.addEdge(nodeId,nid)

	return m

def posToNodeId(row,col,length):
	return (row*length)+col

def genLegalMoves(x,y,length):
	newMoves=[]
	moveOffsets = [(1,0),(0,1),(-1,0),(0,-1)]
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


g=Maze()

start=g.getVertex(35)

BFS(g,start)

def traverse(y):
	x=y
	while x.getPredecessor():
		print x.id, x.getDistance()
		x=x.getPredecessor()
	print x.id, x.getDistance()

traverse(g.getVertex(0))