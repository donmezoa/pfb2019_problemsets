#!/usr/bin/env python3

import glob
import re


blast_files = glob.glob('*.txt')

#print(blast_files)

homology_line = []

for files in blast_files:
	for lines in open(files,"r"):
		lines = lines.rstrip()
#		print(lines)
		if lines.startswith("#"):
			continue
		else: 
			lines = lines.split('\t')
			paresed_lines = lines[1:7]
			homology_line.append(paresed_lines)





print(homology_line)


