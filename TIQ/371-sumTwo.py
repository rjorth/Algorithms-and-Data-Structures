def getSum(a, b):
	stack = [] 
	stack.append(a)
	stack.append(b)
	return sum(stack)
print(getSum(200, 344))
