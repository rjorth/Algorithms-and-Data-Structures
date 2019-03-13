def numJewelsInStones(j, s):
	s = s.lower() 
	j = j.lower() 
	count = 0
	stack = []
	for element in range(len(j)):
		stack.append(j[element])
	for i in range(len(s)):
		 if s[i] in stack: 
		 	count += 1 
	return count  

print(numJewelsInStones("Kan", "kNa"))