def powerOfThree(n):

#if it's a power, then it should be divisble by zero until n is 1
	while (n % 3 == 0): 

		n /= 3 

	return n == 1 

print(powerOfThree(45))