def evaluate(s, flag, memo):
	if len(s) == 0:
		return 0
	if len(s) == 1:
		if int(s) == flag:
			return 1
		else:
			return 0

	# Using memo to reduce the time complexity
	# as there are many duplicate recursions.
	if s + str(flag) in memo:
		return memo[s + str(flag)] 

	ways = 0
	for i in range(1,len(s),2):
		left = s[:i]
		right = s[i+1:]

		leftTrue = evaluate(left, True, memo)
		rightTrue = evaluate(right, True, memo)
		leftFalse = evaluate(left, False, memo)
		rightFalse = evaluate(right, False, memo)

		total = (leftTrue + leftFalse) * (rightTrue + rightFalse)

		totalTrue = 0
		if s[i] == '^':
			totalTrue = (leftTrue * rightFalse) + (leftFalse * rightTrue)
		elif s[i] == '&':
			totalTrue = (leftTrue * rightTrue)
		elif s[i] == '|':
			totalTrue = (leftTrue * rightTrue) + (leftFalse * rightTrue) + (leftTrue * rightFalse)

		if flag == True:
			subways = totalTrue
		else:
			# totalFalse
			subways = total - totalTrue

		ways+=subways

	memo[s + str(flag)] = ways
	return ways


memo = {}
print evaluate('1^0|0|1', False, memo)
print evaluate('0&0&0&1^1|0', True, memo)


