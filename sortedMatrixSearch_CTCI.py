def matrix_search(matrix, x):
	row = 0
	col = len(matrix) - 1

	while row<len(matrix) and col>=0:
		if matrix[row][col] == x:
			return row, col
		elif matrix[row][col] > x:
			col-=1
		else:
			row+=1

	return -1

print matrix_search([[15,20,40,85], [20,35,80,95], [30,55,95,105], [40,80,100,120]], 55)