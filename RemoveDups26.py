from collections import OrderedDict
def removeDups(nums):
	arr = set(nums)
	return (len(arr))

	#set does not work on leetcode because the items must be changed in place

def remove(nums):
	nums[:] = OrderedDict.fromkeys(nums).keys()
	return len(nums)

print(removeDups([1,2,1,2,1,2]))
print(remove([1,2,1,2,1,2]))


