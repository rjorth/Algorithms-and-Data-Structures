def majorityElement(nums): 
	half = len(nums) // 2 
	nums = sorted(nums)

	return nums[half]

print(majorityElement([3,2,3]))
print(majorityElement([2,2,1,1,1,2,2]))