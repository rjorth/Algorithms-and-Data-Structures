

def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, num in enumerate(nums):
            if target - num in d:
                return d[target-num], i
            d[num] = i 


print(twoSum([1,2,3,4], 5))