 """"
 Leetcode:
 Given an array of integers, return indices of the 
 two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.
 """

def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target:
                    if i != j:
                        return i, j
                        print(i, j)


print(twoSum([1,2,3,4], 5))