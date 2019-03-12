def singleNumber(nums):
	# in lambda, ^ is == XOR. When you have 2 of the same number, ^ returns 0 
	return reduce(lambda x,y: x ^ y, nums)

print(singleNumber([2,2,1,1,3,3,4])) 