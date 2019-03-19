def twoSum(nums, target):
    d = {}
        
    for index, val in enumerate(nums):
        if target - val in d: 
            return d[target-val], index
            
    	d[val] = index 

print(twoSum([2,7,11,15], 9))