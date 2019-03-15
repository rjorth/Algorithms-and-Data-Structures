def reverse(head):
	prev = None
	while head:
		cur = head #point
		head = head.next #jump
		cur.next = prev #reverse process
		prev = cur 
	return prev 