def hasCycle(head):
	#use try and except to catch pointer at -1

	try:
		slow = head
		fast = head.next 
		while slow is not fast:
			slow = slow.next
			fast = fast.next.next #skip
		return True 
	except:
		return False 