def fizzbuzz(n):

	d = {3: "Fizz", 5:"Buzz"}
	stack = [] 

	for num in range(1, n+1):
		s = "" #result per number 

		for key in d.keys():
			#if its divisble, get val from stack, either fizz or buzz 
			if num % key == 0:
				s += d[key] #result equals fizz or buzz 

		if not s:
			s = str(num) #result is just a number 

		stack.append(s) #push all the results to a stack 

	return stack 