def distributedCandies(candies):
	n = len(candies) // 2 #split equally between 2 people
	arr = set(candies) #get unique values
	if len(arr) < n: #if fewer unique values than candies, return 
		return len(arr)
	return n #if more candies than unique values, return half 
print(distributedCandies([1,1,2,2,3,3]))
