def validp(s):
	stack = []  #store iterated vals
	#dict is obvious
	d = {
	"]":"[",
	"}":"{",
	")":"("

	}
	#iterate through input
	#if a left holding bracker is crossed, then push 
	#if a right holding bracket is crossed, check that stack is empty
	#if stack is empty, then false bc no left holding
	#otherwise, most recent val must be corresponding left holding
	#return if stack empty, true, if stack contains, false 

	for element in s:
		if element in d.values():
			stack.append(element)
		elif element in d.keys():
			if stack == [] or d[element] != stack.pop():
				return False 
	#stack is empty, then symmetric 
	return stack == [] 