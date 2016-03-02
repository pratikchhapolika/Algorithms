# Graph made manually by mapping out all the moves the knight can make. 
# graph = {'1': ['6', '8'],  
# 		  '2': ['7', '9'],  
# 		  '3': ['4', '8'],
# 		  '4': ['3', '9', '0'],
# 		  '6': ['1', '7', '0'],
# 		  '7': ['2', '6'],
# 		  '8': ['1', '3'],
# 		  '9': ['4', '2'],
# 		  '0': ['4', '6']
# 		 }

########################################################
# This part created the graph using the concept of 
# co-ordinate geometry

graph={}
from graph import Graph
f=open('g.txt','r')
l=[i[:-1] for i in f]
def Maze():  #bdsize is the board size
	m=Graph()
	row_length=len(l)
	col_length=len(l[0])
	for row in range(row_length):
		for col in range(col_length):
			if l[row][col]!='*' and l[row][col]!='#':
				nodeId=posToNodeId(row,col,col_length)
				newPositions=genLegalMoves(row,col,row_length,col_length)
				for i in newPositions:
					nid=posToNodeId(i[0],i[1],col_length)
					if nid!=10 and nid!=12:
						m.addEdge(nodeId,nid)
	f.close()
	return m

def posToNodeId(row,col,length):
	return ((row*length)+col)+1

def genLegalMoves(x,y,row_length,col_length):
	newMoves=[]
	moveOffsets = [(-1,-2),(-1,2),(-2,-1),(-2,1),( 1,-2),( 1,2),( 2,-1),( 2,1)]
	for i in moveOffsets:
		newX=x+i[0]
		newY=y+i[1]
		if legalCoordx(newX,row_length) and legalCoordy(newY,col_length):
			newMoves.append((newX,newY))
	return newMoves

def legalCoordx(x,length):
	if x>=0 and x<length:
		return True
	else:
		return False

def legalCoordy(x,length):
	if x>=0 and x<length:
		return True
	else:
		return False

g=Maze()
for i in g:
	for j in i.getConnections():
		if j.id==11:
			j.id=0
		if str(i.id) in graph:
			graph[str(i.id)].append(str(j.id))
		else:
			graph[str(i.id)]=[str(j.id)]

############################################################


p=[]
l=[]
# this functions does a simple dfs traversal
def dfsvisit(graph,start,x,path=[]):
	path=path+[start]

	if len(path)==x:
		return path

	for newvertex in graph[start]:
		new=dfsvisit(graph,newvertex,x,path)
		l.append(new)
	return l

# x signifies the length of phone number
x=2
for i in [1,2,3,4,6,7,8,9]:
	p.append(dfsvisit(graph,str(i),x))

print p[-1]


