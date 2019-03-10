def majorityElement(nums):
	return sorted(nums)[len(nums) // 2]

print(majorityElement([1,1,1,1,2,2,2]))