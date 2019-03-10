def searchInsert(nums, target): 
	# my solution.... 
	for i in range(len(nums)):
		if nums[i] >= target:
			return i

	return i+1 #if last value in list

def SearchInsertFast(nums, target):
	#leetcode faster python3 solution
	return(sorted(nums + [target]).index(target))

print(searchInsert([1,2,3,4], 5))
print(SearchInsertFast([1,2,3,4], 5))