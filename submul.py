from graph import Graph
from queue import Queue

def operations(start,target):
	g=Graph()
	q=[start]
	right=True
	while right:
		current=q.pop()
		sub=current-1
		mul=current*2
		if sub!=target:
			g.addEdge(current,sub)
		else:
			g.addEdge(current,sub)
			right=False

		if mul!=target:
			g.addEdge(current,mul)
		else:
			g.addEdge(current,mul)
			right=False

		q.insert(0,sub)
		q.insert(0,mul)

	return g

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

s=4
t=8
graph=operations(s,t)
start=graph.getVertex(s)
BFS(graph,start)

def traverse(y):
	x=y
	while x.getPredecessor():
		print x.id, x.getDistance()
		x=x.getPredecessor()
	print x.id, x.getDistance()

traverse(graph.getVertex(t))