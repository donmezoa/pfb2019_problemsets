#!/usr/bin/env python3

dna = 'GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCT'

dna = dna.upper()


def gc_content(dna):
	c_count = dna.count('C')
	g_count = dna.count('G')
	dna_len = len(dna)
	gc_content = (c_count + g_count) / dna_len 
	return gc_content

gc_content(dna)
print(gc_content)







