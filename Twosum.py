def twoSum(nums, target):
	d = {}
	for i, n in enumerate(nums):
		if target - n in d:
			return d[target-n], i
		d[n] = i

print(twoSum([1,2,3,4,5], 3))
