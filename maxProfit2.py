def profit(prices):
	#easy to understand, slow runtime 
	profit = 0 
	for i in range(1, len(prices)):
		if prices[i] > prices[i-1]:
			profit += prices[i] - proces[i-1]
	return profit 