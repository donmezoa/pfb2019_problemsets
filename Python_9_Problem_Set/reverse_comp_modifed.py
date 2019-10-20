#!/usr/bin/env python3

import sys


input_file = ''
try:
	input_file = sys.argv[1]
	print("User provided file:" , input_file)
	if not input_file.endswith('.fa'):
		raise ValueError("Not a FASTA file")
except:
	print("Please provide a file name")

output_file = ''
try:
	output_file = sys.argv[2]
	print("User provided output file:" , output_file)
	if not output_file.endswith('.fa'):
		raise ValueError("Not a FASTA file")
except:
	print("Please provide an output file name")



with open(input_file,"r") as seq_read, open(output_file,"w") as seq_write:
	for line in seq_read:
		line = line.split('\t')
		dna = line[1]
		reverse = dna[::-1]
		new_first_line = line[0] + "_This_is_the_reverse_complement"
		seq_write.write(new_first_line + '\t' +  reverse + '\n')
