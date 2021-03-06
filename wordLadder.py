from graph import Graph,Vertex
from queue import Queue

def buildGraph(wordfile):
	g=Graph()
	d={}          # format is:- {bucket:[wordlist]}
	wfile=open(wordfile,'r')

	# creating the bucket
	for line in wfile:
		word=line[:-1]        # strips the spaces at the end of each line.
		for i in range(len(word)):
			bucket=word[:i]+"_"+word[i+1:]    # creating the bucket
			if bucket in d:
				d[bucket].append(word)
			else:
				d[bucket]=[word]

	# connecting the words in the same bucket
	for bucket in d:
		for word1 in d[bucket]:
			for word2 in d[bucket]:   # because this is an undirected graph
				if word2!=word1:
					g.addEdge(word1,word2)

	return g


g=buildGraph('a.txt')
start=g.getVertex('fool')

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

traverse(g.getVertex('sage'))

