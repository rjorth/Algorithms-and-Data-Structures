def mergeTwoLists(l1, l2):
	temp = cur = ListNode(0)
	while l1 and l2: #while not empty 
		if l1.val < l2.val: #approach smaller value
			temp.next = l1 #store smaller value in temp
			l1 = l1.next #move forward
		else:
			temp.next = l2  #store smaller value
			l2 = l2.next  #move forward

		#move temp list forward
		temp = temp.next 
	temp.next = l1 or l2 
	return cur.next 

print(mergeTwoLists([1,2,4], [1,3,4]))



