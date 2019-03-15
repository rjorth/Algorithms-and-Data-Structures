def climbStairs(n):
	#use 2 pointers 

	a = b = 1 

	for i in range(n):
		a,b = b, a+b 
	return a 

print(climbStairs(3))