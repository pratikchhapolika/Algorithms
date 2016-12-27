# USING DYNAMIC PROGRAMMING
# def boards(k, total, shorter, longer, length, memo):
# 	if k==0:
# 		length.add(total)
# 		return

# 	key = str(k) + " " + str(total)
# 	if key in memo:
# 		return

# 	else:
# 		boards(k-1, total+shorter, shorter, longer, length, memo)
# 		boards(k-1, total+longer, shorter, longer, length, memo)
# 		memo.add(key)


# length = set()
# memo = set()
# boards(2, 0, 1, 2, length, memo)
# print length


# USING SIMPLE FOR LOOP
# MOST INTUITIVE SOLUTION
# RUNNING IN O(N)
def diving_boards(k, shorter, longer):
	result = set()
	for i in range(k+1):
		length = i*shorter + (k-i) * longer
		result.add(length)
	print result

diving_boards(3, 1, 2)