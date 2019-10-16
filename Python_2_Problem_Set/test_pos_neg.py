#!/usr/bin/env python3

# This script will test if a value is positive or negative. 

import sys

# Get first command line parameter.
test_num = sys.argv[1]

# Convert test_num to integer
# if test_num is greater then 0 
if int(test_num) > 0:
	print("Number is positive")
	if int(test_num) < 50:
		print("Number is also less then 50")
		if int(test_num)%2 == 0:
			print("Number is an even number that is smaller then 50")
		elif int(test_num) < 50: 
			print("Number is also greater then 50")
		if int(test_num)%3 == 0:
			print("Number is larger then 50 and divisible by 3") 
elif int(test_num) == 0:
	print("Number is Zero")
else:
	print("Number is negative")

