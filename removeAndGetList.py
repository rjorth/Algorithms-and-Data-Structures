def newNumsList(nums, val):
	stack = [] 
	for i in nums:
		if i != val:
			stack.append(i)
	print(len(stack))
	return stack 


def newStrsList(strs, val):
	stack = [] 
	for i in strs:
		if i != val:
			stack.append(i)
	print (len(stack))
	return stack 

print(newNumsList([4,1,2,3,4], 4))
print(newStrsList(["run", "go", "run", "run"], "run"))
