#optimized solution from leetcode 

def numsInJewels(j, s): 
	return sum(i in j for i in s)

print(numsInJewels("can run", "run"))