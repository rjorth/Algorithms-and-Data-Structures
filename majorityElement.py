def majorityElement(nums):
	#majority must take up more than half
        #sort array 
        #majority element will be stored in middle of the array 
        # // operator rounds to integer
	return sorted(nums)[len(nums) // 2]

print(majorityElement([1,1,1,1,2,2,2]))