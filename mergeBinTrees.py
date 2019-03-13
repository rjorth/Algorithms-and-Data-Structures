def mergeTrees(t1, t2):
	#purpose to add values of trees together 
	if t1 and t2:
		t1.val += t2.val 
		t1.left = mergeTrees(t1.left, t2.left)
		t1.right = mergeTrees(t1.right, t2.right)
	if not t1:
		return t2
	return t1 