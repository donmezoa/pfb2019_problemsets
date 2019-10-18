#!/usr/bin/env python3


# Define variables
factorial = 1
count = 1000

# Determine the factorial
while count > 1:
	factorial = factorial * count
	count-=1

print(factorial)

odd = 0
even = 0



numbers = [101,2,15,22,95,33,2,27,72,15,52]
for number in numbers:
	if number%2 == 0:
#		print(number , "is even")
		even = even + number
	else:
#		print(number , "is odd")
		odd = odd + number
 
print("Sum of even numbers:" , even)
print("Sum of odd numbers:" , odd)




