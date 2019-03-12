def containsDuplicate(nums):
	if not nums:
		return False 

	return len(nums) > len(set(nums))

print(containsDuplicate([1,2,2,3,3]))
print(containsDuplicate([1,2,3]))