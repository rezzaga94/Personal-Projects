import timeit



def fibonacci(n):
	a = 0
	b = 1
	for i in range(0, n):
		temp = a
		a = b 
		b = temp + b 
	return a  
	
	
start = timeit.default_timer()
user_inp = int(input("Please Enter a Number: "))


nums = []

for c in range(0,user_inp):
	nums.append(fibonacci(c))

print("The Fibonacci Sequence up to:", user_inp)	
for c in range(0, user_inp):
	print(fibonacci(c))

print("*************************")

print("The golden ratio up to:", user_inp)	
for c in range(2, len(nums)):
	print((nums[c]/nums[c-1]))

print("*************************")
# print(nums)


print("Calculations took: ",timeit.default_timer() - start, "seconds")

