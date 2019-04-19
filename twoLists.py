def twoLists(arr1, arr2):
	return abs(sum(arr1) - sum(arr2))

print(twoLists([1,2,3],[1,2])) #3
print(twoLists([1,2,],[1,2,3])) #3
print(twoLists([1,2,3,4,5,6,7],[1,2,3,4,5,6])) #7
print(twoLists([0,0,0,1],[1,2,0,0,0])) #2
print(twoLists([1,2,3],[1,2,3,4])) #4
print(twoLists([1,2,3],[1,2,3,1])) # 1

def reverseastring(s): 
	return s[::-1]

print(reverseastring("hello"))
print(reverseastring("tsum"))
print(reverseastring("evorp"))
print(reverseastring("a"))
print(reverseastring("tniop"))
print(reverseastring(""))