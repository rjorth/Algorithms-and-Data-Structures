def reverse(x):
	sign = [-1, 1][x < 0] 

	make_pos = abs(x)

	make_s = str(make_pos)

	make_reverse = make_s[::-1]

	make_int = int(make_reverse)

	return make_int 

print(reverse(211))
