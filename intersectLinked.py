def getIntersect(heada,headb):
	pa = heada
	pb = headb 

	if heada is None or headb is None:
		return None 
	while pa is not pb:
		if pa is None:
			pa = headb
		else:
			pa = pa.next
		if pb is None:
			pb = heada
		else:
			pb = pb.next
	return pa