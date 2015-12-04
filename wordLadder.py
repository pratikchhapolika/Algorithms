from graph import Graph

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

	for i in g:
		print i 

buildGraph('a.txt')
