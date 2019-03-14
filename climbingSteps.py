def climbStairs(n):
	#determine number of ways to reach step 1
	#determine number of ways to reach step 2 
	a = b= 1 

	for _ in range(n):
		a,b = b, a+ b #this must be a same line assertion 
		#else b = a+b with new assignment to a, or b = new assignment b 
	return a 

print(climbStairs(3))