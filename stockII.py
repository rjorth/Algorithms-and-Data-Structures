def maxProfit(prices):
	if len(prices) <= 1:
		return 0 
 
	profit = 0 

	if prices[0] > prices[1]:
		cur = prices[1]
		start = 2 
	else:
		start = 1
		cur = prices[0] 

	for i in range(start, len(prices)):
		if prices[i] < prices[i-1]:
			profit += prices[i-1] - cur
			cur = p[i] 

	profit += p[-1] - cur 

	return profit 