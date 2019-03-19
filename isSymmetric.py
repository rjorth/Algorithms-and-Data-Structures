def isSymmetric(root):
	if root:
		return helper(root.left, right.right)
	else:
		return True

def helper(p, q):
	if p and q:
		return p.val == q.val and
		helper(p.left, q.right) and helper(p.right, q.left)
	else:
		return not p and not q 