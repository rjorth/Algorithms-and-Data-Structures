def strStr(haystack, needle):

	nee = len(needle)

	for i in range(len(haystack) - nee + 1):
		if haystack[i:i + nee] == needle:
			return i 

	return -1 

print(strStr("running", "un"))