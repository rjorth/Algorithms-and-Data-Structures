def mergeLinkedListsSingle(l1,l2):
	cur = temp = ListNode(0) #establish to get structure
	
	while l1 and l2: 
		if l1.val < l2.val:
			#not temp. always next
			temp.next = l1
			l1 = l1.next
		else:
			#always next
			temp.next = l2
			l2 = l2.next
		#set current to next
		temp = temp.next
	#get nxt
	temp.next = l1 or l2
	return cur.next
	
