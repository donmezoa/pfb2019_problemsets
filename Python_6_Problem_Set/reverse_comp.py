#!/usr/bin/env python3

with open("Python_06.seq.txt","r") as seq_read, open("Python_06.rev.seq.txt","w") as seq_write:
	for line in seq_read:
		line = line.split('\t')
		dna = line[1]
		reverse = dna[::-1]
		new_first_line = line[0] + "_This_is_the_reverse_complement"
		seq_write.write(new_first_line + '\t' +  reverse + '\n')
