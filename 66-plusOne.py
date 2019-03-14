def plusOne(digits):

	#tricky part here is 9

	if len(digits) == 0:
		digits = [1] 

	elif digits[-1] == 9:
		digits = plusOne(digits[:-1])
		digits.extend([0])

	else:
		digits[-1] += 1 
	return digits 




print(plusOne([9]))

