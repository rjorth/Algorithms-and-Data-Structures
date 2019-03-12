def maxProfit(prices): 
	maxi, mini = 0, float('inf')
	for i in prices:
		mini = min(mini, i)
		profit = i - mini 
		maxi = max(maxi, profit)
	return maxi 

print(maxProfit([1,2,3,4,5]))
print(maxProfit([5,2,3,2,1]))