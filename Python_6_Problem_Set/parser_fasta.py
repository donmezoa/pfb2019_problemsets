#!/usr/bin/env python3

import sys

fasta_file = sys.argv[1]

dictionary = {}

with open(fasta_file,"r") as fasta_read, open("sequences.txt","w") as dict_write:
	for line in fasta_read:
		line = line.split('\t')
		header_line = line[0]
		dna = line[1]
		dictionary [header_line] = dna
	for key,value in dictionary.items():
		final_dict = key,value
		print(key,value)
		print(dictionary[key]
		dict_write.write(final_dict) 






