def reverseList(head):

	#iterative solution, one day i'll be brave and use recursion
	#ever
	#but not today 
	prev = None 

	while head:
		cur = head
		head = head.next
		cur.next = prev 
		prev = cur 
	return prev 