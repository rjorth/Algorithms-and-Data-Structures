import collections 

def findLHS(nums):
	#counter counts the number of times that an element appears in the list
	#you constantly confuse this with enumerate
	count = collections.Counter(nums)
	#store result
	arr = 0 
	for i in count:
		if i+1 in count:
			arr = max(arr, count[i] + count[i+1])
	return arr


print(findLHS([1,1,1,2,2,2,6]))