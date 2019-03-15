def valid(s): 
	s = s.lower()
	s = s.strip().split(" ")
	s = "".join(s)

	return s == s[::-1]



print(valid("Run on"))
print(valid("race car"))