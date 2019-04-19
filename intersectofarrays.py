def intersect(nums1, nums2):
	nums1, nums2, = sorted(nums1), sorted(nums2)

	p = pt = 0 

	res = [] 

	while True:
		try:
			if nums2[p] > nums2[pt]:
				pt += 1 
			elif nums1[p] < nums2[pt]:
				p += 1 
			else:
				res.append(nums1[pt])
				p += 1
				pt += 1
		except IndexError:
			break 
	return res