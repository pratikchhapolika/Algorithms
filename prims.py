from graph import Graph,Vertex
from priorityQueue import PriorityQueue

def prim(graph,start):     # it belongs to the family of greedy algorithms
	pq=PriorityQueue()
	for v in graph:
		v.setDistance(sys.maxsize)
		v.setPredecessor(None)
	start.setDistance(0)
	pq.buildHeap([(v.getDistance(),v) for v in graph])
	while not pq.isEmpty()
		currentvertex=pq.delMin()
		for newvertex in currentvertex.getConnections():
			newDist=currentvertex.getWeight(newvertex)
			if newDist<newvertex.getDistance() and newvertex in pq:
				newvertex.setDistance(newDist)
				newvertex.setPredecessor(currentvertex)
				pq.decreaseKey(newvertex,newDist)


