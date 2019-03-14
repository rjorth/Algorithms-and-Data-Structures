def validp(s):
	stack = [] 
	d = {
	"]":"[",
	"}":"{",
	")":"("

	}

	for element in s:
		if element in d.values():
			stack.append(element)
		elif element in d.keys():
			if stack == [] or d[element] != stack.pop():
				return False 
	#stack is empty, then symmetric 
	return stack == [] 