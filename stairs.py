def climbStairs(n):
	# a is the number of ways to reach the first step
	# b is the number of ways to reach the next step 
	# after a step, b becomes a, and is reassinged a + b 
	a = b = 1
	for _ in range(n):
		a, b = b, a + b 
	return a 

print(climbStairs(5))