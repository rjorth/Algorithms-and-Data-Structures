def moveZeroes(nums):
	#iterate backwards! 
	for i in range(len(nums))[::-1]:
		if nums[i] == 0:
			#pop where i is zero. does this count as in place?  
			nums.pop(i)
			nums.append(0)
	return nums

print(moveZeroes([1,2,1,0,0,3]))