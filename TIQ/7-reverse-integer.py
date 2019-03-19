def reverse(x):
	sign = [1,-1][x < 0] #if x is less than zero, sign is negative 1 
	n = str(abs(x))
	n = [::-1][n]

	if n > 2 ** 31 - 1:
		return 0 
	else:
		return n * sign 