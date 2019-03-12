def deleteDuplicates(head):
	tracker = head 
	while tracker.next:
		if tracker.val == tracker.next.val:
			tracker.next = tracker.next.next
		tracker = tracker.next 
	return head 

print(deleteDuplicates([1,1,2]))