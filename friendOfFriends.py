a=input()
friend=[]
friend_of_friends=[]
while a>0:
	b=raw_input()
	array=map(int,b.split())
	friend.append(array[0])	
	friend_of_friends.extend(array[2:])
	a-=1

print len(set(friend_of_friends).difference(set(friend)))

