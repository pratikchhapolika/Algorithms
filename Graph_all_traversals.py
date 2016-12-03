def recursive_dfs(graph, start, path=[]):
	'''recursive depth first search from start'''
	path=path+[start]
	for node in graph[start]:
		if not node in path:
			path=recursive_dfs(graph, node, path)
	return path

def iterative_dfs(graph, start, path=[]):
	'''iterative depth first search from start'''
	q=[start]
	while q:
		v=q.pop(0)
		if v not in path:
			path=path+[v]
			q=graph[v]+q
	return path

	
def bfs_paths(graph, start, goal):
	connected = []
	for key,value in graph.items():
		connected.extend(value)

	if not goal in connected:
		return -1

	queue = [(start, [start])]
	while queue:
		vertex, path = queue.pop(0)
		for next in graph[vertex]:
			if next == goal:
				return path + [next]
			else:
				queue.append((next, path + [next]))


'''
	 +---- A
	 |   /   \
	 |  B--D--C
	 |   \ | /
	 +---- E
'''
graph = {'A':['B','C','D'],'B':['D','E'],'C':['D','E'],'D':['E'],'E':['A'], 'F':[]}

print 'recursive dfs ', recursive_dfs(graph, 'A')
print 'iterative dfs ', iterative_dfs(graph, 'A')
print 'iterative bfs ', bfs_paths(graph, 'A', 'E')


