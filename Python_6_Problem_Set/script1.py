#!/usr/bin/env python3


with open("Python_06.txt","r") as file_object, open("Python_06_uc.txt","w")as file_write:
	for line in file_object:
		line = line.rstrip()
		uppercase_line = line.upper()
		print(uppercase_line)
		file_write.write(uppercase_line + "\n")

