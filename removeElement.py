def removeElement(nums, val):
    i = 0 
    n = len(nums)
    while (i < n):
        if nums[i] == val:
            nums[i] = nums[i-n]
            n -= 1
        else:
            i += 1
    return nums 

print(removeElement([1,2,3,4,4,4,5,5,6], 1))