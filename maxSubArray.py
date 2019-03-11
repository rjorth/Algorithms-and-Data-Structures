def getMax(nums):
	#when you start at 1, you keep in place 
	for i in range(1, len(nums)):
		if nums[i-1] > 0:
			nums[i] += nums[i-1]

	return max(nums)


print(getMax([1,2,-3,3,4]))
print(getMax([1,2,3,-4,5,0,7]))
print(getMax([50,60,-40,-4,5,0,7]))

