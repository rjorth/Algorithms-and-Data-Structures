def hasCycle(head):
	slow = fast = head 

	#two pointer solution
	#slow should never catch fast if there is not a cycle 
	
	while slow and fast and fast.next:
		slow = slow.next 
		fast = fast.next.next #keeps just 1 spot ahead 
		if slow == fast:
			return True

	return False 