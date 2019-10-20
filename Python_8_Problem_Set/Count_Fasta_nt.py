#!/usr/bin/env python3

import re

final_dictionary = {}
Individual_gene_dict = {}


with open("Python_08.fasta","r") as file_object:
	for line in file_object:
		line = line.rstrip()
		dict_in = {}
		if re.search(r">", line):
			key_line = line			
			dict_in[key_line] 
#			print(dict_in)
		else:
			nt_count = {}
			for nt in line:
				if nt in nt_count:
					previous_count = nt_count[nt]
					new_count = previous_count + 1
					nt_count[nt] = new_count
				else:
					nt_count[nt] = 1;
		dict_in[key_line]=nt_count
		









