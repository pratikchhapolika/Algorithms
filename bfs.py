from graph import Graph,Vertex
from queue import Queue

def sample():
	g=Graph()
	g.addEdge('a','b')
	g.addEdge('a','c')
	g.addEdge('b','a')
	g.addEdge('b','d')
	g.addEdge('b','e')
	g.addEdge('c','a')
	g.addEdge('c','f')
	g.addEdge('d','b')
	g.addEdge('e','b')
	g.addEdge('e','f')
	g.addEdge('f','c')
	g.addEdge('f','e')

	return g

g=sample()
start=g.getVertex('f')

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

BFS(g,start)

def traverse(y):
	x=y
	while x.getPredecessor():
		print x.id
		x=x.getPredecessor()
	print x.id

traverse(g.getVertex('a'))


