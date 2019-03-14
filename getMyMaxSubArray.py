def getmax(nums):
	#comment code endlessly, to remember thought process through the future
	#instead of working it out in head again
	#comment ALL code, even simple code! 

	#begin at 1 in range
	#check prev, this way don't run out of index
	for i in range(1, len(nums)):
		if nums[i-1] > 0:
			nums[i] += nums[i-1]

	print(nums)

	return max(nums) 

print(getmax([-2,1,-3,4,-1,2,1,-5,4]))
