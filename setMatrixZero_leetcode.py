def setMatrixZero(mat):
	rowHasZero = False
	colHasZero = False

	row = len(mat)
	col = len(mat[0])

	for i in range(col):
		if mat[0][i] == 0:
			rowHasZero = True

	for i in range(row):
		if mat[i][0] == 0:
			colHasZero = True


	for i in range(1, row):
		for j in range(1, col):
			if mat[i][j] == 0:
				mat[i][0] = 0
				mat[0][j] = 0

	for i in range(1, col):
		if mat[0][i] == 0:
			for j in range(row):
				mat[j][i] = 0

	for i in range(1, row):
		if mat[i][0] == 0:
			for j in range(col):
				mat[i][j]=0

	if rowHasZero:
		for i in range(col):
			mat[0][i] = 0

	if colHasZero:
		for i in range(row):
			mat[i][0] = 0

	print mat


setMatrixZero([[1,0,1], 
			   [1,1,1],
			   [1,1,1]])


setMatrixZero([[0,0,0,5],
			   [4,3,1,4],
			   [0,1,1,4],
			   [1,2,1,3],
			   [0,0,1,1]])