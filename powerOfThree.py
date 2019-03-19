def powerOfThree(n):

#if it's a power, then it should be divisble by zero until n is 1
	if n < 1:
		return False #or else time limit exceeded 
	while (n % 3 == 0): 

		n /= 3 

	return n == 1 

print(powerOfThree(45))