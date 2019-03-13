def singleNumber(nums):

	#get sum of unique set * 2 
	#get sum of nums * 
	unique = sum(set(nums)) * 2
	sumNum = sum(nums) 
	result = unique - sumNum 
	return result


print(singleNumber([2,2,3]))