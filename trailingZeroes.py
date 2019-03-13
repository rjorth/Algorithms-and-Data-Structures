class Solution(): 
	def trailingZeroes(self, n):
		#trailing zero is a result of factors 5 * 2 

		#helped solutio n
		assert n >= 0, n
		zeroes = 0
		q = n

		while q:
			q //= 5 
			zeroes += q
		return zeroes  




n = 5
print(Solution().trailingZeroes(n))