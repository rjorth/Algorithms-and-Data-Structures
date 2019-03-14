def merge(nums1, m, nums2, n):
	for i in range(m):
		if nums1[i] == 0:
			if nums2[i] not in nums1:
				nums1[i] = nums2[i]  

print(merge([1,2,3,0,0,0], 6, [2,5,6],3))