def cross(current_position, jump_step, stones, d, target):
	if (current_position, jump_step) in d:
		return False
	
	if current_position == target:
		return True
		
	if current_position not in stones:
		return False
	
	if current_position<0 or current_position>target or jump_step<1:
		return False
	
	possible_jumps = [jump_step-1, jump_step, jump_step+1]
	
	for jump in possible_jumps:
		if cross(current_position+jump, jump, stones, d, target):
			return True

	d.add((current_position, jump_step))
	return False
		
def canCross(stones):
	if len(stones) == 0:
		return True
	if stones[1]!=1:
		return False
	
	d=set()
	
	return cross(1, 1, stones, d, stones[-1])

print canCross([0,1,3,5,6,8,12,17])
