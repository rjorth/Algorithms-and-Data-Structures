def twoSum(nums, target):
    d = {}
        
    for index, val in enumerate(nums):
        if target - val in d: 
            return d[target-val], index
            
    	d[val] = index
    	#only passes all cases when this line is here, and not
    	#first in the loop. 

print(twoSum([2,7,11,15], 9))