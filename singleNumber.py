def singleNumber(nums):

	#get sum of unique set * 2 
	#get sum of nums * 
	#since we know there are exactly 2 copies of every number,
	#we know we need exactly 2 copies to get them back 
	#when you take every unique value and multiply it by two, the only difference in sum
	#will be that 1 original value which isn't already multiplied by 2
	#during the sumNum summation of the list 
	unique = sum(set(nums)) * 2
	sumNum = sum(nums) 
	result = unique - sumNum 
	return result


print(singleNumber([2,2,3]))