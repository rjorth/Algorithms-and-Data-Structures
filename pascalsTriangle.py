def generate(num_rows):

	#result is an array of rows 
	result = [] 

	#first/last num of each row is always 1 

	for num in range(num_rows):
		row = [None for _ in range(num + 1)] #fills every space with 'None'
		row[0], row[-1] = 1, 1 

		for j in range(1, len(row)-1):
			row[j] = result[num - 1][j-1] + result[num-1][j]

		result.append(row)
	return result




print(generate(3))