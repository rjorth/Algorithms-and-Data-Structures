def getMax(nums):
	#start at 1 for this 
	for i in range(1, len(nums)):
		#this is where you struggle most
		#to explain:
		#must start at range 1 if going to check at i - 1, to ensure index
		#if 0 or equal to zero, addition is useless, skip and return
		#if continues, then big enough array to be worth iteration 
		if nums[i-1] >= 0:
			nums[i] += nums[i-1]
	return max(nums)