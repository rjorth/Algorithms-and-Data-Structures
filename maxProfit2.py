def profit(prices):
	#easy to understand, slow runtime 
	profit = 0 
	for i in range(1, len(prices)):
		if prices[i] > prices[i-1]:
			profit += prices[i] - proces[i-1]
	return profit 

def oneLine(prices):
	arr = [] 
	for i in range(len(prices)-1):
		if prices[i+1] > prices[i]:
			profit = prices[i+1] - prices[i] 
			arr.append(profit)
	return sum(arr)


print(oneLine([7,1,5,3,6,4]))