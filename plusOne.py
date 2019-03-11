def plusOne(digits): 

	#add element if empty
	if len(digits) == 0: 
		digits = [1] 

	#allocate space with element 0 
	#recursive, ^^ will change 0 to 1 
	elif digits[-1] == 9: 
		digits = plusOne(digits[:-1])
		digits.extend([0])

	#otherwise 
	else:
		digits[-1] += 1 
	return digits

print(plusOne([9]))
print(plusOne([]))