n=50
# 1's in the array indicate that the index is prime
# 0 indicates that it is composite
primes=[1]*(n+1)

primes[0]=0
primes[1]=0

square_root=n**0.5
for i in range(2,int(square_root)+1):
	if primes[i]==1:
		for j in range(2,n+1):
			if i*j<=n:
				primes[i*j]=0
			else:
				break

count=0
for index,i in enumerate(primes):
	if i==1:
		print index
		count+=1

print "The number of primes are: {}".format(count)