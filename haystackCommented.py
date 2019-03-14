def haystacking(haystack, needle):
	n_len = len(needle)
	get_range = len(haystack) - n_len + 1 

	for i in range(get_range):
		if haystack[i:i+n_len] == needle:
			return i
	return -1 

print(haystacking("hello", "ll"))