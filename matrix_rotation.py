mat= [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]
print mat[::-1]
rotated90 = zip(*mat[::-1])
print rotated90
