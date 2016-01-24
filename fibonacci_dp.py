# MEMOIZATION APPROACH
memo={}
def fib(n):
	if n in memo:
		return memo[n]
	if n<=2:
		memo[n]=1
	else:
		memo[n]=fib(n-1)+fib(n-2)

	return memo[n]

print fib(100)

# BOTTOM-UP APPROACH
# def fibonacci(n):
# 	fib={}
# 	for i in range(1,n+1):
# 		if i<=2:
# 			f=1
# 		else:
# 			f=fib[i-1]+fib[i-2]
# 		fib[i]=f

# 	return fib[n]

# print fibonacci(10)