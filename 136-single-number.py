def singleNumber(nums):
	doublesum = (sum(set(nums))) * 2 
	fairsum = sum(nums) 

	return doublesum - fairsum 
print(singleNumber([1,1,2,2,3]))