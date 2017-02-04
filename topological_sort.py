def topological(graph):         # recursive dfs with 
	l = []                      # additional list for order of nodes
	visited = {u:'white' for u in graph}
	cycle = [False]    
	for u in graph:
		if visited[u] == 'white':
			dfs_visit(graph, u, visited, l, cycle)
		if cycle[0]:
			return []

	l = l[::-1]
	return l                     # l contains the topological sort
 
 
def dfs_visit(graph, u, visited, l, cycle):
	if cycle[0]:
		return

	visited[u] = 'gray'
	
	for v in graph[u]:
		if visited[v] == 'gray':
			cycle[0] = True
			return
		if visited[v] == 'white':
			dfs_visit(graph, v, visited, l, cycle)
	
	visited[u] = 'black'
	l.append(u)  


# # GRAPH WITHOUT CYCLE
graph = {5:[2,0],
		 4:[0,1],
		 2:[3],
		 3:[1],
		 0:[],
		 1:[]
		}


# # GRAPH WITH CYCLE
# # graph = { 0 : [1, 2],
# #            1 : [],
# #            2 : [3],
# #            3 : [4],
# #            4 : [2] }


print topological(graph)

