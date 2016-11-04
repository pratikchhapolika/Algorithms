# Given a set of numbers in an array, 
# First element represents the height of the east most building 
# and next is the building to the west of it and so on. 
# Print the list of buildings that have a 
# sunset view. If a building is shorter than another building 
# to its west then it looses its sunset view.

def sunset(l):
	max_building = l[-1]
	list_of_buildings = [l[-1]]
	for i in range(len(l)-2, -1, -1):
		if l[i] > max_building:
			list_of_buildings.append(l[i])
			max_building = l[i]

	print list_of_buildings

sunset([9, 4, 6, 8, 1, 5, 1, 2, 3, 2])
sunset([10,5,3,8])
sunset([9,8,7,6,5,4,3,2,1])
sunset([10,5,9,9])
sunset([1,2,3,4,5])
