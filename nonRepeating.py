def lengthofLongestSubstring(s):
	start = 0
	maxi = 0
	d = {}

	for i in range(len(s)):
		if s[i] in d and start <= d[s[i]]:
			start = d[s[i]] + 1 
		else:
			maxi = max(maxi, i-start + 1)

		d[s[i]] = i 

	return maxi 
print(lengthofLongestSubstring("pwwkew"))