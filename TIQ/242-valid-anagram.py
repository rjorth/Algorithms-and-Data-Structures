def isAnagram(s,t):
	return sorted(t) == sorted(s)

print(isAnagram("crate","trace"))