from priorityQueue import PriorityQueue
from graph import Graph,Vertex

def sample():
	g=Graph()
	g.addEdge('a','b',2)
	g.addEdge('a','d',3)
	g.addEdge('b','a',2)
	g.addEdge('d','a',3)
	g.addEdge('b','c',1)
	g.addEdge('d','c',2)
	g.addEdge('c','b',1)
	g.addEdge('c','d',2)

	return g

def Dijkstras(graph,start):   
	pq=PriorityQueue()
	start.setDistance(0)
	pq.buildHeap([(v.getDistance(),v) for v in graph])   # distance is the key in the priority queue
	while not pq.isEmpty():
		currentvertex=pq.delMin()
		for newvertex in currentvertex.getConnections():
			newDist=currentvertex.getDistance()+currentvertex.getWeight(newvertex)
			if newDist<newvertex.getDistance(): 
				# at the start the distance of all the vertices is set to maximum. That's why the if statement will be executed
				newvertex.setDistance(newDist)
				newvertex.setPredecessor(currentvertex)
				pq.decreaseKey(newvertex,newDist)


g=sample()
start=g.getVertex('a')
Dijkstras(g,start)

def traverse(y):
	x=y
	while x.getPredecessor():
		print x.id, x.getDistance()
		x=x.getPredecessor()
	print x.id, x.getDistance()

traverse(g.getVertex('c'))
