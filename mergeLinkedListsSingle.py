def mergeLinkedListsSingle(l1,l2):
	cur = temp = ListNode(0) #establish to get structure
	#honestly, ^^ is most confusing part of alg for you 

	#this is a two pointer problem
	#GET USED TO TWO POINTERS. 

	while l1 and l2: #you usually get this far, idiot 
		if l1.val < l2.val: #you can get here for the most part/ more or less
			temp.next = l1 #hold this val in list 
			l1 = l1.next  #while held, move forward 
		else: #meaing val of l1 is greater than val at l2, so l2.val should come first
			temp.next = l2
			l2 = l2.next 
		temp = temp.net 
	temp.next = l1 or l2 #if odd
	return cur.next 
	
