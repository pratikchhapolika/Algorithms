class Vertex(object):

	def __init__(self,key):
		self.id=key
		self.connectedTo={}   # format is:- {key:value} => {vertex:weight}

	def add_neighbour(self,vertex,weight):
		self.connectedTo[vertex]=weight

	def __str__(self):
		return str(self.id)+" is connected to "+str([x.id for x in self.connectedTo])

	def getConnections(self):  # getVertices
		return self.connectedTo.keys()  # gets the keys i.e. vertices

	def getId(self):
		return self.id

	def getWeight(self,vertex):
		return self.connectedTo[vertex]  # gets the value i.e weight

class Graph(object):

	def __init__(self):
		self.vertList={}
		self.numVertices=0

	def addVertex(self,key):
		self.numVertices+=1
		newVertex=Vertex(key)    # newVertex is an object.
		self.vertList[key]=newVertex    # an object is assigned to vertList(key)
		return newVertex

	def getVertex(self,n):
		if n in self.vertList:
			return self.vertList[n]
		else:
			return None

	def __contains__(self,n):
		return n in self.vertList

	def addEdge(self,f,t,cost=0):  # f is the first vertex and  t is the second vertex
		if f not in self.vertList:
			nv=self.addVertex(f)
		if t not in self.vertList:
			nv=self.addVertex(t)
		self.vertList[f].add_neighbour(self.vertList[t],cost)   # this is a directed graph

	def getVertices(self):
		return self.vertList.keys()

	def __iter__(self):          # to make graph object(g) iterable
		return iter(self.vertList.values())


# g=Graph()
# for i in range(6):
# 	g.addVertex(i)
# g.addEdge(0,1,5)
# g.addEdge(0,5,2)
# g.addEdge(1,2,4)
# g.addEdge(2,3,9)
# g.addEdge(3,4,7)
# g.addEdge(3,5,3)
# g.addEdge(4,0,1)
# g.addEdge(5,4,8)
# g.addEdge(5,2,1)
# for v in g:
# 	print v
# 	# for w in v.getConnections():
# 	# 	print "%s, %s"%(v.getId(),w.getId())
