#!/usr/bin/env python3

import sys


dna = sys.argv[1]
width = int(sys.argv[2])

#final_format = ''

save_write = "DNA_" + str(width) + "_nt.fa"


def define_nt_length(dna):
	final_format = ''	
	for nt in dna:
	#	final_format += nt
		nt = nt.rstrip()
		if (len(final_format)%width==0 and len(final_format)!=0):
			final_format += '\n'		
		else:
			final_format += nt
	with open (save_write, "w") as file_object: 
		file_object.write (final_format)
	return define_nt_length

define_nt_length(dna)
print('Your FASTA file is now', width)










