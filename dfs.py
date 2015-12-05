from graph import Graph,Vertex

class DFSGraph(Graph):
	
	def __init__(self):
		super(DFSGraph,self).__init__()
		self.time=0

	def DFS(self):
		for avertex in self:
			avertex.setColor('white')
			avertex.setPredecessor(-1)
		for avertex in self:
			if avertex.getColor()=='white':
				self.dfsvisit(avertex)

	def dfsvisit(self,startvertex):
		startvertex.setColor('gray')
		self.time+=1
		startvertex.setDiscovery(self.time)
		for newvertex in startvertex.getConnections():
			if newvertex.getColor()=='white':
				newvertex.setPredecessor(startvertex)
				self.dfsvisit(newvertex)

		startvertex.setColor('black')
		self.time+=1
		startvertex.setFinish(self.time)


d=DFSGraph()

d.addEdge('a','b')
d.addEdge('a','c')
d.addEdge('b','a')
d.addEdge('b','d')
d.addEdge('b','e')
d.addEdge('c','a')
d.addEdge('c','f')
d.addEdge('d','b')
d.addEdge('e','b')
d.addEdge('e','f')
d.addEdge('f','c')
d.addEdge('f','e')

d.DFS()
for i in d:
	print i

def traverse(y):
	x=y
	while x.getPredecessor():
		print x.id
		x=x.getPredecessor()
	print x.id

traverse(d.getVertex('f'))


# def sample():
# 	g=Graph()
# 	g.addEdge('a','b')
# 	g.addEdge('a','c')
# 	g.addEdge('b','a')
# 	g.addEdge('b','d')
# 	g.addEdge('b','e')
# 	g.addEdge('c','a')
# 	g.addEdge('c','f')
# 	g.addEdge('d','b')
# 	g.addEdge('e','b')
# 	g.addEdge('e','f')
# 	g.addEdge('f','c')
# 	g.addEdge('f','e')

# 	return g

# def DFS(g):
# 	for i in g:
# 		i.setColor('white')
# 		i.setPredecessor(-1)
# 	for i in g:
# 		if i.getColor()=='white':
# 			dfsvisit(i)

# def dfsvisit(start):
# 	time=0
# 	start.setColor('gray')
# 	time+=1
# 	start.setDiscovery(time)
# 	for newvertex in start.getConnections():
# 		if newvertex.getColor()=='white':
# 			newvertex.setPredecessor(start)
# 			dfsvisit(newvertex)

# 	start.setColor('black')
# 	time+=1
# 	start.setFinish(time)

# gr=sample()
# DFS(gr)

# def traverse(y):
# 	x=y
# 	while x.getPredecessor():
# 		print x.id
# 		x=x.getPredecessor()
# 	print x.id

# traverse(gr.getVertex('f'))