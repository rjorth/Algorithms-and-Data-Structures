import sys 
x = int(sys.argv[1])
n = x
m = x
tree = 0
beers = 0

while(n > 0 ):
	beers = beers + n
	n = n-1
temp = beers
while (temp > 0):
	tree = tree + temp
	temp = temp - m
	m = m - 1

x = str(x)
beers = str(beers)
tree = str(tree)
print("Level: " + x + "\nBeers: " + beers + "\nTree: " + tree)
