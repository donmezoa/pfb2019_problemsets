#!/usr/bin/env python3

import re

with open("Python_07.fasta","r") as fasta:
	for line in fasta:
		line = line.rstrip()
		if re.search( r"(>\S*)\s*(.*)" ,line):
			line_list = re.search( r"(>\S*)\s*(.*)" ,line):			
				id_list = line.group(1)
				print(id_list)




			#header = line
#			id_list = line.group(1)
#			print(id_list)
		#desc_list = header.group(2)
		#print(desc_list)		
		#if header:
#		print(header)
#		id_list = header.group(1)
#		print(id_list)
#		desc_list = header.group(2)
#		print(desc_list)

#seq_name_desc = "id:",id_list," desc:",id_list

