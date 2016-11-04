def topological(graph):         # recursive dfs with 
	l = []                      # additional list for order of nodes
	visited = {u:False for u in graph}    
	for u in graph:
		if visited[u] == False:
			dfs_visit(graph, u, visited, l)
 
	l = l[::-1]
	return l                     # l contains the topological sort
 
 
def dfs_visit(graph, u, visited, l):
	visited[u] = True
	for v in graph[u]:
		if visited[v] == False:
			dfs_visit(graph, v, visited, l)

	l.append(u)  


graph = {5:[2,0],
		 4:[0,1],
		 2:[3],
		 3:[1],
		 0:[],
		 1:[]
		}

print topological(graph)

