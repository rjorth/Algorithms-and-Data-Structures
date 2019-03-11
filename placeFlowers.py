def placeFlowers(flowerbed, n):
	if n == 0 : 
		return True

	flowerbed = [0] + flowerbed + [0] 
	for i in range(1, len(flowerbed)-1):
		if flowerbed[i-1] == flowerbed[i] == flowerbed[i+1] == 0:
			flowerbed[i] = 1 
			n -= 1
			if n == 0: 
				return True
	return False 

print(placeFlowers([1,0,0,0,1], 1))