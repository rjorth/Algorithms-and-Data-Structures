def isHappy(n):
	
	#get unique values, prevents loop from going infinitely
	seen = set()
	while n != 1:
		n = sum([int(i) ** 2 for i in str(n)])
		if n in seen:
			return False 
		else:
			seen.add(n)
	else:
		return True
	
	


print(isHappy(19))
print(isHappy(0))