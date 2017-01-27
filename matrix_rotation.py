def rotate(matrix):
	n = len(matrix) - 1
	for row in range(len(matrix)/2):
		for col in range(row, len(matrix)-1-row):
			temp = matrix[row][col]

			matrix[row][col] = matrix[n-col][row]
			
			matrix[n-col][row] = matrix[n-row][n-col]
			
			matrix[n-row][n-col] = matrix[col][n-row]
			
			matrix[col][n-row] = temp

	print matrix

rotate([[1,2,3],
		[4,5,6],
		[7,8,9]])



# mat= [[1, 2, 3],
#       [4, 5, 6],
#       [7, 8, 9]]
# print mat[::-1]
# rotated90 = zip(*mat[::-1])
# print rotated90
