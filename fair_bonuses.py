# You manage a team of developers and you have to give concert tickets as a bonus to the developers. 
# For each developer, you know how many lines of code he/she wrote the previous week, 
# and you want to reward more productive developers.

# The developers sit in a row. Each developer, except the first and last, has two neighbors. 
# You must give each developer one or more tickets in such a way that if a developer has written 
# more lines of code than a neighbor, then he/she receives more tickets than his/her neighbor.

# Compute the minimum number of tickets you need to buy to satisfy the constraint. 
# For example, if Andy, Bob, Charlie and David sit in a row from left to right, 
# and the previous week they wrote 300, 400, 500, and 200 lines of code respectively, 
# then Andy and David should receive 1 ticket each, Bob should receive 2 tickets, 
# and Charlie should receive 3 tickets, for a total of 7 tickets.

def bonus(l):
	left_to_right = [None]*len(l)
	right_to_left = [None]*len(l)
	total_tickets = 0
	final_score = []

	left_to_right[0]=1
	for i in range(1, len(l)):
		if l[i] > l[i-1]:
			left_to_right[i] = left_to_right[i-1] + 1
		elif l[i] == l[i-1]:
			left_to_right[i] = left_to_right[i-1]
		else:
			left_to_right[i] = 1

	right_to_left[len(l)-1] = 1
	for i in range(len(l)-2, -1, -1):
		if l[i] > l[i+1]:
			right_to_left[i] = right_to_left[i+1] + 1
		elif l[i] == l[i+1]:
			right_to_left[i] = right_to_left[i+1]
		else:
			right_to_left[i] = 1

	for i in range(len(l)):
		final_score.append(max(left_to_right[i], right_to_left[i]))

	print sum(final_score)

bonus([300,400,500,200])
bonus([100, 200, 300, 400, 400, 400, 300, 200, 100])
bonus([4,3,2,1])
bonus([400, 400, 300, 300, 200, 200, 100, 100, 200, 200, 300, 300, 400, 400])
bonus([300, 200, 100, 100, 200, 300, 300, 200, 100])


