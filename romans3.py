def toRoman(s):
	roman = {
	"M": 1000,
	"D": 500,
	"C": 100,
	"L" : 50,
	"X": 10, 
	"V": 5,
	"I": 1 
	}
	#get dict, obvious
	pre = 0 
	post = 0
	#set ret, hold return val 

	for i in range(0,len(s)-1): #avoid indexing error
		#loop 0 to length
		#if num in dict less than following num in dict, its to subtract
		if (i < len(s) -1) and roman[s[i]] < roman[s[i+1]]:
			result -= roman[s[i]]
		else:
			#if num in dict greater than following, then to add 
			result += roman[s[i]]
	#get result, plus final addition which is always an add 
	return result + roman[s[-1]]