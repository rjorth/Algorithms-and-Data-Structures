def mysqrt(x):
	if not x:
		return 0 
	x = x ** (0.5)
	x = int(x) 
	return x 

print(mysqrt(5))