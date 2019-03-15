def reverse(s):
	s = list(s)
	i,j = 0, len(r) - 1 

	while i < j:
		s[i], s[j] = s[j], s[i]
		i += 1
		j -= 1 
	s= "".join(s)