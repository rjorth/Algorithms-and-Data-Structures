def getIntersection(heada, headb):
	if heada is None or headb is None:
		return None 

	pa = heada #pointer
	pb = headb #pointer

	while pa is not pb:
		#move next until head 
		if pa is None:
			pa = headb 
		else:
			pa.next
		if pb is None:
			pb = heada
		else:
			pb.next 

	return pa 