def validStrPalindrome(s):
	#.isalnum() checks that each character is either a number or letter, nice
	#.join() can only be applied to strings (originally, you tried to go
	#strip.split( " ")) and rejoin in the list. this way, keep a string 
	s = "".join([c.lower() for c in s if c.isalnum()])
	return s == s[::-1]

print(validStrPalindrome("race a away "))
print(validStrPalindrome("racecar"))
print(validStrPalindrome("Dad daD"))
print(validStrPalindrome("T8 8T"))
print(validStrPalindrome("going swimming"))