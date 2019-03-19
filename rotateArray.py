def rotate(nums, k):
	temp = previous = 0

	for i in range(k):
		previous = nums[len(nums) -1]

		for j in range(len(nums)):
			temp = nums[j]
			nums[j] = previous 
			previous = temp 