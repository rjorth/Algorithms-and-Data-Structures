def runningsum(nums):
	n = 0
	while n < len(nums): 
		nums[n] += nums[n-1]
		n += 1
	return nums 

print(runningsum([1,2,3,4]))


