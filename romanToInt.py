def romanToInt(s):
	#make dict to store vals  
	roman = {
	"M": 1000,
	"D": 500,
	"C": 100,
	"L" : 50,
	"X": 10, 
	"V": 5,
	"I": 1 
	}

	#sum total of letters 
	result = 0 
	for i in range(0, len(s) - 1):
		##determine whether vals mean to subtract or add
		if roman[s[i]] < roman[s[i+1]]:
			result -= roman[s[i]]
		else:
			result += roman[s[i]]

	return result + roman[s[-1]] 



	


print(romanToInt("I"))
print(romanToInt("V"))
