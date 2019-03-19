def first(s):
	count = collections.Counter(s)
	index = 0
	for char in s:
		if count[char] == 1:
			return index
		else:
			index += 1 
	return -1 