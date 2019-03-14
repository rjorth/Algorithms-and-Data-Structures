def merge(t1,t2):
	#add vals of trees

	#if both have values then :
	if t1 and t2:
		#combine vals as long as both have vals available
		t1.val += t2.val
		t1.left = merge(t1.left, t2.left)
		t1.right = merge(l2.right, t2,right)
		#obviously interchangeable

	#we default to t1. if t1 is not, then go for t2. but mostly return t1 
	if not t1:
		return t2
	return t1 