def maxp(prices):
	if len(prices) < 2: 
		return 0 

	result = 0 
	buy = prices[0] 

	for price in prices[1:]:
		if price > buy:
			result = max(result, price - buy)
		else:
			buy = price 
	return result 

print(maxp([7,1,5,3,6,4]))