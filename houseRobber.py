def rob(nums):

	maxi = max(nums)
	total = 0
	for i in nums:

		if i == maxi:
			while i+1 and i-1:
				total += sum(maxi, i+1,)
				total += sum(i-1)
	return total

print(rob([1,2,3,1]))