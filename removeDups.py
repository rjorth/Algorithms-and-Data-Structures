from collections import OrderedDict

def remove(nums):
	nums[:] = OrderedDict.fromkeys(nums).keys()
	return len(nums)


print(remove([1,1,2,1])) #2
print(remove([])) #0
print(remove([1,1,2,2,2,3])) #3
print(remove([50])) #1
print(remove([1,1,1,1,1,2,1])) #2 
