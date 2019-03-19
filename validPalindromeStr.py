def valid(s):
	s = s.lower()
	s = s.strip().split(' ')
	s = "".join(char for char in s if char.isalnum())
 

	return s == s[::-1]

print(valid("Race car"))
print(valid("fat"))
print(valid(":racecar"))

