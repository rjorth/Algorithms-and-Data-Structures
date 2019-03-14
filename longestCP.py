def longCP(strs):
	if not strs:
		return ""


	#min from a list of strings will return the value with the shortest common prefix 
	#likewise, max does the opposite
	min_prefix = min(strs)
	max_prefix = max(strs)

	if not min_prefix: #nothing in common, so remove 
		return ""
	#if there isn't a minimum prefix, then there isn't a prefix at all.
	#this is also why we only need to check 2 values, instead of iterating the whole list

	for i in range(len(min_prefix)):
		if max_prefix[i] != min_prefix[i]:
			return max_prefix[:i]
	return min_prefix[i]

print(longCP(["flower","flow","flowt"]))