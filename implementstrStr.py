def strStr(haystack, needle):
	if not needle:
		return 0 
	leedle = len(needle) #needle length

	for i in range(len(haystack)):
		if haystack[i:i+leedle] == needle:
			return i
	return -1 

print(strStr("coffee", "co"))
print(strStr("coffee", "ff"))
print(strStr("coffeeff", "ff"))