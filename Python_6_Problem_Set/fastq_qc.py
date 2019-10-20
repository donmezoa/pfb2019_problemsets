#!/usr/bin/env python3

lines = 0
characters = 0


with open("Python_06.fastq","r") as seq_read:
	for line in seq_read:
		line = line.rstrip()
		lines = lines + 1
		characters = len(str(line)) + characters

print("Number of lines:", lines)
print("Number of characters:", characters)
print("Average line length:", characters / lines)
