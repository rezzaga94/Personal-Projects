import timeit

start = timeit.default_timer()

def fibonacci(n):
	if n <= 1:
		return n 
	else:
		return(fibonacci(n-1) + fibonacci(n-2))


user_inp = int(input("Enter a number: "))
print("Fibonacci sequence up to ", user_inp)
for i in range(user_inp):
	print(fibonacci(i))
	
stop = timeit.default_timer()

print(stop - start)