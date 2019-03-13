def sockMerchant(ar):
	array = sorted(ar)
	half = len(ar) // 2 
	if array[half] == 'U':
		return "below"
	else:
		return "above"

print(sockMerchant("UDDDUDUU")) 