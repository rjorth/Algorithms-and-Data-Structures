def reverse(x): 
	#if x is negative, sign = -1 
	#if x is positive, sign = 1 
	sign = [1,-1][x<0]

	pos = abs(x) #make x positive 
	s = str(pos) #make x iterable 
	rev = s[::-1] # reverse x 

	result = int(rev) * sign #return x to an integer of its sign 
	return result 

print(reverse(-123))
print(reverse(56789))
print(reverse(-43509098))
print(reverse(-1234530))